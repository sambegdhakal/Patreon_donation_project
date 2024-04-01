from django.shortcuts import render
from django.http import JsonResponse
from .models import User

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            return JsonResponse({'error': 'Username already exists.'}, status=400)
        else:
            new_user = User.objects.create(username=username, password=password)
            return JsonResponse({'message': 'User registered successfully!'})
    else:
        return render(request, 'registration_form.html')
