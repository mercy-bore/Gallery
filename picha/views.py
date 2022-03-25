from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
import datetime as dt

def welcome(request):
    return HttpResponse('Welcome to My Gallery')

def display_image(request):
    date = dt.date.today()  
    html = f'''
        <html>
            <body>
                 <h1> Picture posted on  {date.day}-{date.month}-{date.year}</h1>
                <h1><img src="https://www.freecodecamp.org/news/content/images/size/w2000/2021/08/chris-ried-ieic5Tq8YMk-unsplash.jpg"</h1>
            </body>
        </html>
            '''
    return HttpResponse(html)

def past_days_images(request,past_date):
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
    # Converts data from the string Url
    date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()

    day = (date)
    html = f'''
        <html>
            <body>
                <h1>Pictures for {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
    return HttpResponse(html)