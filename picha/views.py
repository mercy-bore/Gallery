from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Image,Category,Location
import datetime as dt

def gallery(request):
    return render(request, 'gallery.html')

def display_image(request):
    category = Category.objects.all()
    image = Image.objects.all()
    return render(request,'all-images.html',{'image':image,'category':category})

def search_results(request):
    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        results = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": results})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except:
        raise Http404()
    return render(request,"photo.html", {"image":image})