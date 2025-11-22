from django.contrib import admin
from .models import APIToken, Collector

# Register your models here.
admin.site.register(APIToken)
admin.site.register(Collector)
