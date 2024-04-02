# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import PatreonPage
from registration.models import PatreonUser


def patreon_page_list(request):
    user = PatreonUser.objects.get(username = request.session["user"])
    pages = PatreonPage.objects.filter(creator=user)
    return render(request, 'pagelist.html', {'pages':pages})

# @login_required
# def patreon_page_detail(request, pk):
#     page = get_object_or_404(PatreonPage, pk=pk)
#     return render(request, 'patreon/page_detail.html', {'page': page})


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
            return redirect('patreon_page_list')
    return render(request, 'createpage.html')

# @login_required
# def patreon_page_update(request, pk):
#     page = get_object_or_404(PatreonPage, pk=pk)
#     if request.method == 'POST':
#         title = request.POST.get('title')
#         description = request.POST.get('description')
#         goal_amount = request.POST.get('goal_amount')
#         if title and description and goal_amount:
#             page.title = title
#             page.description = description
#             page.goal_amount = goal_amount
#             page.save()
#             return redirect('patreon_page_list')
#     return render(request, 'patreon/page_form.html', {'page': page})

def patreon_page_delete(request, pk):
    page = get_object_or_404(PatreonPage, pk=pk)
    if request.method == 'POST':
        page.delete()
        return redirect('patreon_page_list')
    return render(request, 'patreon/page_confirm_delete.html', {'page': page})