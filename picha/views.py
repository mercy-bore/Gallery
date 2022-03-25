from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
import datetime as dt

def welcome(request):
    return HttpResponse('Welcome to My Gallery')

def display_image(request):
    html = f'''
        <html>
            <body>
                <h1><img src="https://www.freecodecamp.org/news/content/images/size/w2000/2021/08/chris-ried-ieic5Tq8YMk-unsplash.jpg"</h1>
            </body>
        </html>
            '''
    return HttpResponse(html)
