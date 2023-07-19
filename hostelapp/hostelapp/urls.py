"""hostelapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from SelectionApp import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('home/', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('availability/<str:hostel>/', views.availability, name='availability'),
    path('availability/<str:hostel>/room_form/', views.room_form, name='room_form'),
    path('amenities/', views.amenities, name='amenities'),
    path('mess/', views.mess, name='mess'),
    path('login/', views.user_login, name='login'),
    path('room_confirmation/', views.room_confirmation, name='room_confirmation'),
    path('contact/', views.contact, name='contact'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('room/form/<int:room_id>/', views.room_form, name='room_form'),
]