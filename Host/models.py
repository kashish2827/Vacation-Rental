from django.db import models
from core.models import User
# Create your models here.
class Host(models.Model):
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    )

    host = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    earnings = models.FloatField(default=0.0)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return self.host.username
    
class Property(models.Model):
    PROPERTY_TYPE_CHOICES = (
        ('villa', 'Villa'),
        ('apartment', 'Apartment'),
        ('homestay', 'Homestay'),
        ('farmhouse', 'Farmhouse'),
    )

    STATUS_CHOICES = (
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('maintenance', 'Maintenance'),
    )

    AVAILABILITY=(
        ('booked','Booked'),
        ('notbooked','Not Booked')
    )

    host = models.ForeignKey(Host, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField()
    location = models.CharField(max_length=150)
    price = models.FloatField()
    amenities = models.TextField()
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPE_CHOICES)
    availability = models.CharField(max_length=50, choices=AVAILABILITY)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES)

    def __str__(self):
        return self.title
    
class LocalExperience(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=150)
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.name