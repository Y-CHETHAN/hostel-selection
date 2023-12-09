from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver

class Hostel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Room(models.Model):
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE)
    room_number = models.CharField(max_length=10)
    room_type = models.CharField(max_length=10, blank=True)
    availability = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.room_type:
            self.room_type = self.room_number
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.room_number} - {self.hostel.name}"

class Student(models.Model):
    name = models.CharField(max_length=100)
    registration_number = models.CharField(max_length=12, unique=True)
    phone_number = models.CharField(max_length=10)
    parent_phone_number = models.CharField(max_length=10)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, blank=True, related_name='students')

    def room_type(self):
        if self.room:
            return self.room.room_type
        return ''

    def __str__(self):
        return self.name

@receiver(post_delete, sender=Student)
def update_room_availability(sender, instance, **kwargs):
    room = instance.room
    if room:
        room.availability += 1
        room.save()

# Connect the signal handler function to the post_delete signal of the Student model
post_delete.connect(update_room_availability, sender=Student)


from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    # Add other fields as needed

    def __str__(self):
        return self.username
