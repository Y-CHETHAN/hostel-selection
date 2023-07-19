from django.contrib import admin
from .models import Hostel, Room, Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'registration_number',
        'phone_number',
        'parent_phone_number',
        'get_room_number',
        'get_room_type',
        'get_hostel',  # Display the hostel information
    )

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

    def get_hostel(self, obj):
        if obj.room and obj.room.hostel:
            return obj.room.hostel.name
        return ''
    get_hostel.short_description = 'Hostel'

admin.site.register(Hostel)
admin.site.register(Room)
