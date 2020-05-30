from django.contrib import admin
from django.urls import path
from myapp import views
urlpatterns = [
    path('home',views.home),
    path('about_us',views.aboutus),
    path('contact_info',views.contact),
    path('home1',views.home1)
]