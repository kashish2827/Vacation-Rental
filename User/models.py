from django.db import models
from core.models import User
from Host.models import Property
# Create your models here.

class Guest(models.Model):
    guest = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    booking_history = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.guest.username
    
class Booking(models.Model):
    BOOKING_STATUS = (
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
    )

    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    booking_status = models.CharField(max_length=15, choices=BOOKING_STATUS)
    total_amount = models.FloatField()

    def __str__(self):
        return f"Booking {self.id}"
    
class Review(models.Model):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    review_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review {self.id}"
    
class Wishlist(models.Model):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.guest} - {self.property}"
