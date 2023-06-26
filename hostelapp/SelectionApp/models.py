from django.db import models

class Hostel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Room(models.Model):
    room_number = models.CharField(max_length=10)
    room_type = models.CharField(max_length=20)
    availability = models.IntegerField()
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE)

    def __str__(self):
        return self.room_number

class Student(models.Model):
    name = models.CharField(max_length=100)
    registration_number = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    parent_phone_number = models.CharField(max_length=20)
    preferred_room_type = models.CharField(max_length=20)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
