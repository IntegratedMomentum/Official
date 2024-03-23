from django.contrib import admin
from django.urls import path
from apptn import views

urlpatterns = [
    path('', views.index, name='index'),
    path('download', views.download, name='download'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('inst', views.inst, name="inst"),
]