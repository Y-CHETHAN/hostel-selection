from django import forms
from .models import Student

class RoomBookingForm(forms.ModelForm):
    room_number = forms.CharField(label='Room Number', widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    room_type = forms.CharField(label='Room Type', widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = Student
        fields = ['name', 'registration_number', 'phone_number', 'parent_phone_number', 'room_number', 'room_type']
        labels = {
            'name': 'Name',
            'registration_number': 'Registration Number',
            'phone_number': 'Phone Number',
            'parent_phone_number': "Parent's Phone Number",
            'room_number': 'Room Number',
            'room_type': 'Room Type',
        }

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class StudentRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2')
        labels = {'username': 'Student ID'}

class StaffRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2')
        labels = {'username': 'Staff ID'}

from .models import Room


class Staff_Booking_Form(forms.ModelForm):
    
    class Meta:
        model = Room
        fields = "__all__"
