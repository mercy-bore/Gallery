from django.urls import re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    re_path('^$',views.welcome,name = 'welcome'),
    re_path(r'^image/$',views.display_image,name='display_image'),
    re_path(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_images,name = 'pastImages'),
    ] 



