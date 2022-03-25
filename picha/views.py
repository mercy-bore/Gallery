from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
import datetime as dt

def welcome(request):
    return HttpResponse('Welcome to My Gallery')
