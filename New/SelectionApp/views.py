from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .models import Hostel, Room, Student
from .forms import RoomBookingForm,Staff_Booking_Form
from django.shortcuts import render, redirect
from .forms import StudentRegistrationForm, StaffRegistrationForm

def landing(request):
    return render(request,"userlog/land.html")

def student_registration(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_student = True
            user.save()
            return redirect('login')
    else:
        form = StudentRegistrationForm()
    return render(request, 'userlog/student_registration.html', {'form': form})

def staff_registration(request):
    if request.method == 'POST':
        form = StaffRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = True
            user.save()
            return redirect('login')
    else:
        form = StaffRegistrationForm()
    return render(request, 'userlog/staff_registration.html', {'form': form})

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import StudentRegistrationForm, StaffRegistrationForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            if user.is_student:
                return redirect('dashboard')
            elif user.is_staff:
                return redirect('dashboard')
            else:
                return redirect('dashboard')
        else:
            # Authentication failed
            return render(request, 'login.html', {'error_message': 'Invalid credentials'})
    
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
    boys_rooms = Room.objects.filter(hostel=boys_hostel, availability__gt=0)

    # Get all unique room types for boys hostel rooms
    room_types = Room.objects.filter(hostel=boys_hostel, availability__gt=0).values_list('room_type', flat=True).distinct()

    # Handle filter form submission
    if request.method == 'GET':
        room_type_filter = request.GET.get('room_type')
        if room_type_filter:
            boys_rooms = boys_rooms.filter(room_type=room_type_filter)

    return render(request, 'availability_boys.html', {'rooms': boys_rooms, 'room_types': room_types})

@login_required(login_url='login')
def availability_girls(request):
    girls_hostel = Hostel.objects.get(name='girls')
    girls_rooms = Room.objects.filter(hostel=girls_hostel, availability__gt=0)

    # Get all unique room types for girls hostel rooms
    room_types = Room.objects.filter(hostel=girls_hostel, availability__gt=0).values_list('room_type', flat=True).distinct()

    # Handle filter form submission
    if request.method == 'GET':
        room_type_filter = request.GET.get('room_type')
        if room_type_filter:
            girls_rooms = girls_rooms.filter(room_type=room_type_filter)

    return render(request, 'availability_girls.html', {'rooms': girls_rooms, 'room_types': room_types})


from django.db.models import Q

@login_required(login_url='login')
def room_form(request, room_id):
    room = get_object_or_404(Room, pk=room_id)

    # Check if the user has an existing booking in either boys or girls hostel
    existing_booking = Student.objects.filter(
        Q(registration_number=request.user.username, room__hostel__name='boys') |
        Q(registration_number=request.user.username, room__hostel__name='girls')
    ).exists()

    if existing_booking:
        return render(request, 'room_form.html', {'form_submitted': True})

    if request.method == 'POST':
        form = RoomBookingForm(request.POST)
        if form.is_valid():
            registration_number = form.cleaned_data['registration_number']
            
            # Check if the user has an existing booking in either boys or girls hostel
            existing_booking = Student.objects.filter(
                Q(registration_number=registration_number, room__hostel__name='boys') |
                Q(registration_number=registration_number, room__hostel__name='girls')
            ).exists()

            if existing_booking:
                return render(request, 'room_form.html', {'form_submitted': True})

            booking = form.save(commit=False)
            booking.name = form.cleaned_data['name']
            booking.user = request.user
            booking.room = room
            booking.save()
            room.availability -= 1
            room.save()

            return render(request, 'room_form.html', {'form_submitted': True, 'room': room})
    else:
        form = RoomBookingForm()

    return render(request, 'room_form.html', {'room': room, 'form': form})

def contact(request):
    return render(request, 'contact.html')

@login_required(login_url='login')
def logout(request):
    messages.info(request, 'You have been logged out.')
    messages.clear(request)
    return redirect('login')

def amenities(request):    
    context = {}
    return render(request, 'amenities.html', context)

def mess(request):    
    context = {}
    return render(request, 'mess.html', context)

def dashboard(request):
    if request.user.is_student:
        # If the logged-in user is a student, display room details
        room_details = Room.objects.all()
        return render(request, 'userlog\dashboard.html', {'room_details': room_details})
    elif request.user.is_staff:
        # If the logged-in user is a staff member, provide students' details
        student_details = Student.objects.all()
        return render(request, 'userlog\dashboard.html', {'student_details': student_details})
    else:
        # Handle other user types or customize as needed
        return render(request, 'userlog\dashboard.html')
    
@login_required(login_url='login')
def staff_Booking(request):
    form = Staff_Booking_Form()
    if request.method == 'POST':
        form = Staff_Booking_Form(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = Staff_Booking_Form()
    return render(request,"Room_allocation.html",{'form':form})
        