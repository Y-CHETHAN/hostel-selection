from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .models import Hostel, Room, Student
from .forms import RoomBookingForm
from django.shortcuts import get_object_or_404


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')

@login_required(login_url='login')
def home(request):
    username = request.user.username
    return render(request, 'home.html', {'username': username})

@login_required(login_url='login')
def availability(request, hostel):
    if hostel == 'boys':
        return availability_boys(request)
    elif hostel == 'girls':
        return availability_girls(request)
    else:
        return redirect('home')

@login_required(login_url='login')
def availability_boys(request):
    boys_hostel = Hostel.objects.get(name='boys')
    boys_rooms = Room.objects.filter(hostel=boys_hostel)
    return render(request, 'availability_boys.html', {'rooms': boys_rooms})

@login_required(login_url='login')
def availability_girls(request):
    girls_hostel = Hostel.objects.get(name='girls')
    girls_rooms = Room.objects.filter(hostel=girls_hostel)
    return render(request, 'availability_girls.html', {'rooms': girls_rooms})

from django.contrib import messages

@login_required(login_url='login')
def room_form(request, room_id):
    room = get_object_or_404(Room, pk=room_id)
    existing_booking = Student.objects.filter(registration_number=request.user.username).exists()
    if existing_booking:
        messages.error(request, 'You have already submitted a room booking.')
        return redirect('home')

    if request.method == 'POST':
        form = RoomBookingForm(request.POST)
        if form.is_valid():
            registration_number = form.cleaned_data['registration_number']
            if Student.objects.filter(registration_number=registration_number).exists():
                messages.error(request, 'Registration number already exists.')
                return redirect('room_form', room_id=room_id)

            booking = form.save(commit=False)
            booking.user = request.user
            booking.room = room
            booking.save()

            room.availability -= 1
            room.save()

            return redirect('room_confirmation')
    else:
        initial_data = {
            'room_number': room.room_number,
            'room_type': room.room_type,
        }
        form = RoomBookingForm(initial=initial_data)

    context = {'room': room, 'form': form}
    return render(request, 'room_form.html', context)





@login_required(login_url='login')
def room_confirmation(request):
    username = request.user.username
    student = Student.objects.filter(registration_number=username).last()
    return render(request, 'room_confirmation.html', {'student': student})



def contact(request):
    return render(request, 'contact.html')

@login_required(login_url='login')
def logout(request):
    messages.clear(request)
    return redirect('login')

def amenities(request):    
    context = {}
    return render(request, 'amenities.html', context)

def mess(request):    
    context = {}
    return render(request, 'mess.html', context)
