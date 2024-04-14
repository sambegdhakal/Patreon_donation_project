from django.http import JsonResponse
from django.shortcuts import render
from .forms import ImageForm

def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            user_id = request.POST.get('user_id')
            image_id = request.POST.get('image_id')
            image = form.save(commit=False)
            image.user_id = user_id
            image.image_id = image_id
            image.image_url = image.image.url
            image.save()
            return JsonResponse({'success': True, 'user_id': user_id, 'image_id': image_id})
        else:
            return JsonResponse({'success': False, 'error': 'Form data is not valid'})
    else:
        user_id = request.GET.get('user_id')  # Get user_id from URL query parameter
        image_id = request.GET.get('image_id')  # Get image_id from URL query parameter
        return render(request, 'upload_image.html', {'user_id': user_id, 'image_id': image_id})
