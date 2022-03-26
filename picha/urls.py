from django.urls import re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    re_path('^$',views.gallery,name = 'gallery'),
    re_path(r'^image/',views.display_image,name='displayImages'),
    re_path(r'^search/', views.search_results, name='search_results'),
    ] 



