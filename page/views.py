# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import PatreonPage
from registration.models import PatreonUser
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.http import JsonResponse
from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_exempt


def patreon_page_list(request):
    user = PatreonUser.objects.get(username = request.session["user"])
    pages = PatreonPage.objects.filter(creator=user)
    data = [{'id': page.id, 'description': page.description, 'goal amount': page.goal_amount, 'creator': page.creator.username} for page in pages]
    return JsonResponse(data, safe=False)

# @login_required
# def patreon_page_detail(request, pk):
#     page = get_object_or_404(PatreonPage, pk=pk)
#     return render(request, 'patreon/page_detail.html', {'page': page})

@csrf_exempt
def patreon_page_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        goal_amount = request.POST.get('goal_amount')
        user = PatreonUser.objects.get(username = request.session["user"])
        if title and description and goal_amount:
            PatreonPage.objects.create(
                title=title,
                description=description,
                goal_amount=goal_amount,
                creator=user
            )
            return JsonResponse({'msg':"page added succesfully"})
    return render(request, 'createpage.html')

@csrf_exempt
def patreon_page_update(request, id):
    page = PatreonPage.objects.get(id=id)
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        goal_amount = request.POST.get('goal_amount')
        print(title)
        if title and description and goal_amount:
            page.title = title
            page.description = description
            page.goal_amount = goal_amount
            page.save()
            messages.success(request, 'Page updated successfully!')
            return JsonResponse({'msg':"page updated succesfully"})
        else:
            messages.error(request, 'Please fill in all fields.')
            return JsonResponse({'msg':"please fill all the fields"})
    return render(request, 'updatepage.html', {'page': page})

@csrf_exempt
def patreon_page_delete(request, id):
    if request.method == 'POST':
        page = get_object_or_404(PatreonPage, pk=id)
        page.delete()
        return JsonResponse({'id':id ,'msg':"deleted"})
    return render(request, 'patreon/page_confirm_delete.html', {'page': page})