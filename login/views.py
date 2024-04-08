from django.shortcuts import render
from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        
        if user is not None:
            # Login successful
            request.session["user"] = username
            return JsonResponse({'message': 'Login successful!', 'username':username})
        else:
            # Login failed
            return JsonResponse({'error': 'username or password did not match'}, status=400)
    else:
        #login page rendered
        return render(request, 'login.html')
