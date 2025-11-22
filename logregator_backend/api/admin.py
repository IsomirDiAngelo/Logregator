from django.contrib import admin
from .models import APIToken, Collector, Log

# Register your models here.
admin.site.register(APIToken)
admin.site.register(Collector)
admin.site.register(Log)
