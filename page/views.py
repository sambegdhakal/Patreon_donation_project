# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import PatreonPage
from registration.models import PatreonUser
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def patreon_page_list(request, username):
    user = PatreonUser.objects.get(username=username)
    pages = PatreonPage.objects.filter(creator=user)
    data = [{'id': page.id, 'title':page.title, 'description': page.description, 'creator_username': page.creator.username, 'current_amount': page.current_amount,'image': page.image.url}
            for page in pages]
    response = JsonResponse(data, safe=False)
    response["Access-Control-Allow-Origin"] = "http://localhost:3000"
    return response


@csrf_exempt
def patreon_page_create(request, userid):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES['image']
        user = PatreonUser.objects.get(userid=userid)
        if title and description:
            page = PatreonPage.objects.create(
                title=title,
                description=description,
                creator=user,
                image=image)
            data = [{'creatorid': page.creator.userid, 'description': page.description, 'creator_username': page.creator.username,
                     'current_amount': page.current_amount, 'pageid': page.id}]
            response = JsonResponse(data,safe=False)
            response["Access-Control-Allow-Origin"] = "http://localhost:3000"
            return response

@csrf_exempt
def patreon_page_update(request, id):
    page = PatreonPage.objects.get(id=id)
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        if title and description:
            page.title = title
            page.description = description
            page.save()
            data = {'creatorid': page.creator.userid, 'description': page.description, 'creator_username': page.creator.username,
                    'current_amount': page.current_amount, 'pageid': page.id}
            response = JsonResponse(data,safe=False)
            response["Access-Control-Allow-Origin"] = "http://localhost:3000"
            return response
        else:
            return JsonResponse({'msg':"page update failed"})

@csrf_exempt
def patreon_page_delete(request, id):
    if request.method == 'POST':
        page = get_object_or_404(PatreonPage, pk=id)
        page.delete()
        response= JsonResponse({'id':id ,'msg':"deleted"})
        response["Access-Control-Allow-Origin"] = "http://localhost:3000"
        return response

@csrf_exempt
def patreon_page_donation(request, id, userid):
    if request.method == 'POST':
        page = PatreonPage.objects.get(id=id)
        donation_amount = request.POST.get('donation_amt')
        page.current_amount = page.current_amount + int(donation_amount)
        page.save()
        user = PatreonUser.objects.get(userid=userid)
        response = JsonResponse({'pageid':id ,'msg':"donation updated"})
        response["Access-Control-Allow-Origin"] = "http://localhost:3000"
        return response

@csrf_exempt
def subscribe_to_page(request, id, userid):
    if request.method == 'POST':
        page = PatreonPage.objects.get(id=id)
        page.subscriber_count += 1
        page.save()
        user = PatreonUser.objects.get(userid=userid)
        response = JsonResponse({'pageid':id ,'msg':"Subscribed"})
        response["Access-Control-Allow-Origin"] = "http://localhost:3000"
        return response