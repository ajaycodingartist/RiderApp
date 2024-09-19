from django.contrib import admin
from .models import Ride

# Register your models here.
@admin.register(Ride)
class RideAdmin(admin.ModelAdmin):
    list_display = ('id', 'rider', 'driver', 'pickup_location', 'dropoff_location', 'status', 'current_location', 'created_at', 'updated_at')
    list_filter = ('status', 'driver')
    search_fields = ('pickup_location', 'dropoff_location', 'rider__username', 'driver__username')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        (None, {
            'fields': ('rider', 'driver', 'pickup_location', 'dropoff_location', 'status', 'current_location')
        }),
        ('Dates', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        # Optionally filter or modify the queryset
        return queryset

    def save_model(self, request, obj, form, change):
        # Optionally modify the save behavior
        super().save_model(request, obj, form, change)