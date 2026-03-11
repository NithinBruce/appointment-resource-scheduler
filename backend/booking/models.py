from django.db import models
from django.contrib.auth.models import User

class Resource(models.Model):
    RESOURCE_TYPE_CHOICES = [
        ('staff', 'Staff'),
        ('room', 'Room'),
        ('equipment', 'Equipment'),
    ]
    name=models.CharField(max_length=100)
    resource_type = models.CharField(max_length=20, choices=RESOURCE_TYPE_CHOICES)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    

class Appointment(models.Model):
    STATUS_CHOICES = [
        ('booked', 'Booked'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)

    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='booked')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.resource}"