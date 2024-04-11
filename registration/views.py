from django.shortcuts import render
from django.http import JsonResponse
from .models import PatreonUser

def userregister(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if PatreonUser.objects.filter(username=username).exists():
            response= JsonResponse({'error': 'Username already exists.'}, status=400)
            return response
        else:
            new_user = PatreonUser.objects.create(username=username, password=password)
            response= JsonResponse({'message': 'User registered successfully!', 'username': new_user.username, 'userid': int(new_user.userid)})
            response["Access-Control-Allow-Origin"] = "http://localhost:3000"
            return response
    #else:
        #return render(request, 'register.html') 