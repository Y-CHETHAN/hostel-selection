from django.contrib import admin
from .models import Hostel, Room, Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'registration_number', 'phone_number', 'parent_phone_number', 'get_room_number', 'get_room_type')

    def get_room_number(self, obj):
        if obj.room:
            return obj.room.room_number
        return ''
    get_room_number.short_description = 'Room Number'

    def get_room_type(self, obj):
        if obj.room:
            return obj.room.room_type
        return ''
    get_room_type.short_description = 'Room Type'

admin.site.register(Hostel)
admin.site.register(Room)
