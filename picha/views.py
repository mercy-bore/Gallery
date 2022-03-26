from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
import datetime as dt

def welcome(request):
    return render(request, 'welcome.html')

def display_image(request):
    date = dt.date.today()
    return render(request, 'todays-images.html', {"date": date,})

def past_days_images(request,past_date):
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(display_image)

    return render(request, 'past-images.html', {"date": date})