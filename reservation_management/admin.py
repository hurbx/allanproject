from django.contrib import admin
import reservation_management.models as models


# Register your models here.

class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'name', 'phone', 'email')


admin.site.register(models.Client, ClientAdmin)


class TourAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'client', 'initial_date', 'final_date', 'hotel', 'hotel_room',
                    'quantity', 'currency', 'price', 'total_price')


admin.site.register(models.Tour, TourAdmin)


class HotelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'phone', 'region', 'city', 'country')


admin.site.register(models.Hotel, HotelAdmin)


class HotelRoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'room_type', 'price', 'description')


admin.site.register(models.HotelRoom)
