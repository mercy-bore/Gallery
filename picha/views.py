from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Image,Category,Location
import datetime as dt

def gallery(request):
    category = Category.objects.all()
    image = Image.objects.all()
    return render(request, 'gallery.html', {'image':image,'category':category})

def display_image(request):
    image = Image.objects.all()
    return render(request,'all-images.html',{'image':image})

def search_results(request):

    
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except:
        raise Http404()
    return render(request,"photo.html", {"image":image})