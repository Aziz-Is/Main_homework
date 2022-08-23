from django.contrib import admin
from .models import Tracker, Status, Type

# Register your models here.
admin.site.register(Tracker)
admin.site.register(Status)
admin.site.register(Type)
