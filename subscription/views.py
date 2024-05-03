# Create your views here.
from django.shortcuts import render
from .models import PatreonSubscription
from registration.models import PatreonUser
from page.models import PatreonPage
from django.http import JsonResponse
import datetime

def patreon_page_subscription(request, userid, pageid, date):
    if request.method == 'POST':
        user = PatreonUser.objects.get(userid=userid)
        page = PatreonPage.objects.get(id=pageid)
        amount = request.POST.get('amt')
        try:
            subscription = PatreonSubscription.objects.get(pagesub=page, subuser=user)
        except PatreonSubscription.DoesNotExist:
            subscription = PatreonSubscription.objects.create(pagesub=page, subuser=user)

        subscription.price= subscription.price + int(amount)
        subdate = datetime.datetime.strptime(date, "%Y-%m-%d").date()
        subscription.date= subdate
        subscription.save()
        response = JsonResponse({'userid':userid ,'pageid':pageid ,'msg':"subscription done",'price': amount, 'dateClosed': date})
        response["Access-Control-Allow-Origin"] = "http://localhost:3000"
        return response
    return render(request, 'subscription.html')
def view_page_subscription(request, pageid):
    try:
        page_subscription = PatreonSubscription.objects.filter(pagesub_id=pageid)
        total_subscription = page_subscription.count()
        response = JsonResponse({'pageid': pageid, 'total_subscription': total_subscription})
    except PatreonSubscription.DoesNotExist:
        response = JsonResponse({'pageid': pageid, 'total_subscription': 0})
    response["Access-Control-Allow-Origin"] = "http://localhost:3000"
    return response