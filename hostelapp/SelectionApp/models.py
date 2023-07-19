from django.db import models

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

