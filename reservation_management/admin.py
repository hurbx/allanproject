from django.contrib import admin
import reservation_management.models as models
# Register your models here.
admin.site.register(models.Client)
admin.site.register(models.Tour)
admin.site.register(models.Hotel)
admin.site.register(models.HotelRoom)

