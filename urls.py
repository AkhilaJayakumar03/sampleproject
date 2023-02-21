from django.urls import path
from.views import *

urlpatterns=[
    path('hello/',hello),
    path('welcome/',first),
    path("page/",second),
    path('reg/',reg),
    path('log/',login),
    path('emp/',emp),
    path('search/',search),
    path('display/',display),
    path('empdisplay/',empdisplay),
    path('imageupload/',imageupload),
    path('imagedisplay/',imagedisplay),
    path('audioupload/',audioupload),
    path('audiodisplay/',audiodisplay),
    path('videoupload/',videoupload)

]