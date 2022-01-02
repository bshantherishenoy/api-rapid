from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views
urlpatterns = [
    path('new/',views.new,name="TaskNew" ),
    path('all/',views.all,name='TaskAll')
]
