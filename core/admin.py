from django.contrib import admin
from .models import Restaurant, Dish, Booking


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ("name", "kitchen", "average_check", "rating", "is_active")
    list_filter = ("kitchen", "is_active")
    search_fields = ("name", "kitchen", "address")


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ("name", "restaurant", "category", "price", "is_available")
    list_filter = ("restaurant", "category", "is_available")
    search_fields = ("name",)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("restaurant", "user", "date", "time", "guests", "status")
    list_filter = ("status", "date", "restaurant")
    search_fields = ("user__username", "restaurant__name")