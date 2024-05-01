# Create your views here.
from django.shortcuts import render
from .models import PatreonDonation
from registration.models import PatreonUser
from page.models import PatreonPage
from django.http import JsonResponse

def patreon_page_donation(request, userid, pageid):
    if request.method == 'POST':
        user = PatreonUser.objects.get(userid=userid)
        page = PatreonPage.objects.get(id=pageid)
        donation_amount = request.POST.get('donation_amt')
        try:
            donation = PatreonDonation.objects.get(pagemodel=page, pageuser=user)
        except PatreonDonation.DoesNotExist:
            donation = PatreonDonation.objects.create(pagemodel=page, pageuser=user)

        donation.current_amount= donation.current_amount + int(donation_amount)
        donation.save()
        response = JsonResponse({'userid':userid ,'pageid':pageid ,'msg':"donation updated",'donated_amt': donation_amount})
        response["Access-Control-Allow-Origin"] = "http://localhost:3000"
        return response

def view_page_amt(request, pageid):
    try:
        page_donations = PatreonDonation.objects.filter(pagemodel_id=pageid)
        total_donation_amount = sum(donation.current_amount for donation in page_donations)
        response = JsonResponse({'pageid': pageid, 'total_donation': total_donation_amount})
    except PatreonDonation.DoesNotExist:
        response = JsonResponse({'pageid': pageid, 'total_donation': 0})
    response["Access-Control-Allow-Origin"] = "http://localhost:3000"
    return response