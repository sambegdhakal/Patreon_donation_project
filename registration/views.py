from django.shortcuts import render
from django.http import JsonResponse
from .models import PatreonUser

def userregister(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        if PatreonUser.objects.filter(username=username).exists():
            return JsonResponse({'error': 'Username already exists.'}, status=400)
        else:
            new_user = PatreonUser.objects.create(username=username, password=password, first_name=first_name, last_name=last_name, email=email)
            return JsonResponse({'message': 'User registered successfully!'})
    else:
        return render(request, 'register.html') #name should match the html file name