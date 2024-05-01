from django.http import JsonResponse, HttpResponseNotAllowed
from .models import PatreonUser
from images.models import Image



def userregister(request):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])
    
    username = request.POST.get('username')
    password = request.POST.get('password')
    if PatreonUser.objects.filter(username=username).exists():
        return JsonResponse({'error': 'Username already exists.'}, status=409)
    else:
        image = Image.objects.create(
            image_file=request.FILES["image"]
        )
        new_user = PatreonUser.objects.create(
            username=username, 
            password=password,
            profile_image=image
        )
        return JsonResponse({
            'message': 'User registered successfully!', 
            'username': new_user.username, 
            'userid': new_user.userid,
            'profile_pic': new_user.profile_image.id,
        })

