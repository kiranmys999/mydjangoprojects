from django.contrib import admin

# Register your models here.
from models import Hotel, Room

myModels = [Hotel, Room]

class RoomInline(admin.TabularInline):
    model = Room


class HotelAdmin(admin.ModelAdmin):
    inlines = [RoomInline]


admin.site.register(Hotel, HotelAdmin)

