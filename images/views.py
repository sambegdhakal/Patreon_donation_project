from .models import Image
from django.http import JsonResponse, HttpResponseNotFound, HttpResponseNotAllowed, HttpResponse


"""
Given an image id, returns the image file

Returns 404 if no accompanying file exists
"""
def get_image(request, imageid):
    if request.method != "GET": 
        return HttpResponseNotAllowed(["GET"])
    
    try:
        image = Image.objects.get(id=imageid)
        with open(image.image_file.path, "rb") as f:
            image_data = f.read()

            file_extension = image.image_file.path.split(".")[-1]

            return HttpResponse(image_data, content_type=f"image/{file_extension}") 
    except Image.DoesNotExist:
        return HttpResponseNotFound()


"""
Given an image file in the body, saves the image to the database

Returns {
    imageid: integer
}
"""
def upload(request): 
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])
    
    image = Image.objects.create(
        image_file=request.FILES["image"]
    )
    return JsonResponse({"imageid": image.id})

    