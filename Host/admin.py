from django.contrib import admin
from .models import Host, Property, LocalExperience
# Register your models here.
admin.site.register(Host)
admin.site.register(Property)
admin.site.register(LocalExperience)