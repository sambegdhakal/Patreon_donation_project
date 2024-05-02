from .models import PatreonPage
from registration.models import PatreonUser
from images.models import Image
from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponse, HttpResponseNotFound


"""
Given a user's ID, return their associated donation page or 404

Returns: {
    'id': integer, 
    'title': string, 
    'description': string, 
    'creatorid': integer,
    'creator_username': string, 
    'creator_profile_id': integer,
    'imageid': integer
}
"""
def patreon_page_view(request, id):
    if (request.method != "GET"):
        return HttpResponseNotAllowed(["GET"])
    
    try:
        user = PatreonUser.objects.get(userid=id)
        page = PatreonPage.objects.get(creator=user)

        data = {
            'id': page.id, 
            'title': page.title, 
            'description': page.description, 
            'creatorid': page.creator.userid,
            'creator_username': page.creator.username, 
            'creator_profile_id': page.creator.profile_image.id,
            'imageid': page.banner_image.id
        }
        return JsonResponse(data, safe=False)
    except PatreonPage.DoesNotExist:
        return HttpResponseNotFound()
    except PatreonUser.DoesNotExist:
        return HttpResponseNotFound()
    

def patreon_page_list(request, username):
    users = PatreonUser.objects.filter(username__icontains=username)
    pages = PatreonPage.objects.filter(creator__in=users)
    data = [{'id': page.id, 'title':page.title, 'description': page.description, 'creator_username': page.creator.username,
             'creatorid': page.creator.userid, 'creator_profile_id': page.creator.profile_image.id, 'imageid': page.banner_image.id}
            for page in pages]
    response = JsonResponse(data, safe=False)
    response["Access-Control-Allow-Origin"] = "http://localhost:3000"
    return response
    

"""
Given a user's ID, creates a donation page for them with JSON
whose fields are defined as: {
    title: string
    description: string
    image: file
}

Returns: {
    'id': integer, 
    'title': string, 
    'description': string, 
    'creatorid': integer,
    'creator_username': string, 
    'creator_profile_id': integer,
    'imageid': integer
}

Returns 409 if an associated page already exists
"""
def patreon_page_create(request, userid):
    if (request.method != "POST"):
        return HttpResponseNotAllowed(["POST"])
    
    user = PatreonUser.objects.get(userid=userid)
    # check to see if the user already has a donation page
    try:
        PatreonPage.objects.get(creator=user)
        # 409 -- conflict
        return HttpResponse(status=409)
    except PatreonPage.DoesNotExist:
        pass
    
    title = request.POST.get('title')
    description = request.POST.get('description')
    image = Image.objects.create(
        image_file=request.FILES["image"]
    )

    page = PatreonPage.objects.create(
        title=title,
        description=description,
        creator=user,
        banner_image=image
    )
    
    data = {
        'id': page.id, 
        'title': page.title, 
        'description': page.description, 
        'creatorid': page.creator.userid,
        'creator_username': page.creator.username, 
        'creator_profile_id': page.creator.profile_image.id,
        'imageid': image.id
    }
    return JsonResponse(data, safe=False)


"""
Given a donation page ID, updates that donation page with JSON
defined as: {
    title: string,
    description: string
}

Any number of those fields can be absent

Returns status 200 if successful
"""
def patreon_page_update(request, id):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])
    
    page = PatreonPage.objects.get(id=id)
    title = request.POST.get('title')
    description = request.POST.get('description')
    
    newImage = None
    try:
        image = request.FILES["image"]
        newImage = Image.objects.create(
            image_file=image
        )
    except:
        pass

    if title: 
        page.title = title
    if description: 
        page.description = description
    if newImage:
        page.banner_image = newImage
    page.save()

    return HttpResponse()


"""
Given a user's ID, tries to delete their associated donation page

Returns status 200 if successful
"""
def patreon_page_delete(request, id):
    if request.method != 'DELETE':
        return HttpResponseNotAllowed(["DELETE"])
    
    PatreonPage.objects.get(id=id).delete()
    return HttpResponse()


def subscribe_to_page(request, pageid, userid):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])

    page = PatreonPage.objects.get(id=pageid)
    page.subscriber_count += 1
    page.save()

    return HttpResponse()