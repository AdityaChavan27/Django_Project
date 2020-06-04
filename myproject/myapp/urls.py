from django.contrib import admin
from django.urls import path
from myapp import views
urlpatterns = [
    path('home',views.home),
    path('about_us',views.aboutus),
    path('contact_info',views.contact),
    path('home1',views.home1),
    path('register/',views.create,name="register"),
    path('success',views.success,name='success'),
    path('show',views.show,name='show'),
    path('delete/<int:id>',views.destroy,name='delete'),
    path('edit/<int:id>',views.edit,name='edit'),

]