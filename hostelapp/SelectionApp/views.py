from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .models import Hostel, Room, Student

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
    hostels = Hostel.objects.all()
    rooms = Room.objects.all()
    return render(request, 'home.html', {'username': username, 'hostels': hostels, 'rooms': rooms})

@login_required(login_url='login')
def room_selection(request):
    username = request.user.username
    if request.method == 'POST':
        # Process room selection logic
        messages.success(request, 'Room successfully booked')
        return redirect('room_confirmation')
    hostels = Hostel.objects.all()
    return render(request, 'room_selection.html', {'username': username, 'hostels': hostels})

@login_required(login_url='login')
def room_confirmation(request):
    username = request.session.get('username')
    student = Student.objects.filter(registration_number=username, room__isnull=False).last()
    return render(request, 'room_confirmation.html', {'student': student})

def payment(request):
    username = request.user.username
    student = Student.objects.filter(room__isnull=False).last()
    if request.method == 'POST':
        # Process payment logic here
        messages.success(request, 'Payment successful')
        return redirect('confirmation')
    return render(request, 'payment.html', {'username': username, 'student': student})

@login_required(login_url='login')
def confirmation(request):
    username = request.user.username
    return render(request, 'confirmation.html', {'username': username})

@login_required(login_url='login')
def payment_error(request):
    username = request.user.username
    return render(request, 'payment_error.html', {'username': username})

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