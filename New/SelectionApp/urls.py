from django.urls import path
from SelectionApp import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("",views.landing,name="landing"),
    path("login/", views.login_view, name='login'),
    path("student/",views.student_registration,name="student_registration"),
    path("staff_reg/",views.staff_registration,name="staff_registration"),
    path("dash/",views.dashboard,name="dashboard"),
    path('Home/', views.home, name='home'),
    path('availability/<str:hostel>/', views.availability, name='availability'),
    path('availability/<str:hostel>/room_form/', views.room_form, name='room_form'),
    path('amenities/', views.amenities, name='amenities'),
    path('mess/', views.mess, name='mess'),
    path('contact/', views.contact, name='contact'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('room/form/<int:room_id>/', views.room_form, name='room_form'),
    path("booking/",views.staff_Booking,name="staff_Booking"),
    # path("chatbot/",views.chatbot,name="chatbot"),
]