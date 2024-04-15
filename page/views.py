# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import PatreonPage
from registration.models import PatreonUser
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def patreon_page_list(request, userid):
    user = PatreonUser.objects.get(userid=userid)
    pages = PatreonPage.objects.filter(creator=user)
    data = [{'id': page.id, 'title':page.title, 'description': page.description, 'goal_amount': page.goal_amount,
            'creator_username': page.creator.username, 'current_amount': page.current_amount,'image': page.image.url} 
            for page in pages]
    response = JsonResponse(data, safe=False)
    response["Access-Control-Allow-Origin"] = "http://localhost:3000"
    return response


@csrf_exempt
def patreon_page_create(request, userid):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        goal_amount = request.POST.get('goal_amount')
        image = request.FILES['image']
        user = PatreonUser.objects.get(userid=userid)
        if title and description and goal_amount:
            page = PatreonPage.objects.create(
                title=title,
                description=description,
                goal_amount=goal_amount,
                creator=user,
                image=image)
            data = [{'creatorid': page.creator.userid, 'description': page.description, 
                     'goal_amount': page.goal_amount, 'creator_username': page.creator.username, 
                     'current_amount': page.current_amount}]
            response = JsonResponse(data,safe=False)
            response["Access-Control-Allow-Origin"] = "http://localhost:3000"
            return response

@csrf_exempt
def patreon_page_update(request, id):
    page = PatreonPage.objects.get(id=id)
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        goal_amount = request.POST.get('goal_amount')
        if title and description and goal_amount:
            page.title = title
            page.description = description
            page.goal_amount = goal_amount
            page.save()
            data = {'creatorid': page.creator.userid, 'description': page.description, 
                    'goal_amount': page.goal_amount, 'creator_username': page.creator.username, 
                    'current_amount': page.current_amount}
            
            response = JsonResponse(data,safe=False)
            response["Access-Control-Allow-Origin"] = "http://localhost:3000"
            return response
        else:
            return JsonResponse({'msg':"page update failed"})
    return render(request, 'updatepage.html', {'page': page})

@csrf_exempt
def patreon_page_delete(request, id):
    if request.method == 'POST':
        page = get_object_or_404(PatreonPage, pk=id)
        page.delete()
        response= JsonResponse({'id':id ,'msg':"deleted"})
        response["Access-Control-Allow-Origin"] = "http://localhost:3000"
        return response
    return render(request, 'patreon/page_confirm_delete.html', {'page': page})

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