from django.contrib import admin
from .models import Guest, Booking, Wishlist, Review
# Register your models here.
admin.site.register(Guest)
admin.site.register(Booking)
admin.site.register(Review)
admin.site.register(Wishlist)