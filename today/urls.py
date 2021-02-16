from django.contrib import admin
from django.urls import path,include
from .views import All,Feras
from django.conf.urls import url
app_name='today'
urlpatterns = [
url(r'^all/$',All,name='all'),
url(r'^feras/$',Feras,name='feras'),
]