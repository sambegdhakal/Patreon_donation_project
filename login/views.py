from django.contrib.auth import authenticate
from django.http import JsonResponse, HttpResponseNotAllowed


def login(request):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])

    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    
    if user is not None:
        return JsonResponse({
            'message': 'Login successful!', 
            'username': user.username, 
            'userid': user.userid,
            'profile_pic': user.profile_image.id,
        })
    else:
        return JsonResponse({
            'error': 'username or password did not match'
        }, status=400)

