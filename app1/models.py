from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Ride(models.Model):
    STATUS_CHOICES = [
        ('requested', 'Requested'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    rider = models.ForeignKey(User, related_name='rider', on_delete=models.CASCADE)
    driver = models.ForeignKey(User, related_name='driver', on_delete=models.SET_NULL, null=True, blank=True)
    pickup_location = models.CharField(max_length=255)
    dropoff_location = models.CharField(max_length=255)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='requested')
    current_location = models.CharField(max_length=255, blank=True)  # For real-time tracking
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Ride {self.id} by {self.rider.username}"
