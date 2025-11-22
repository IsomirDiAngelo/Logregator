from django.db import models
from datetime import datetime
from .api_token import APIToken

class Collector(models.Model):
    name = models.CharField(max_length=10)
    api_token = models.OneToOneField(APIToken, on_delete=models.CASCADE, primary_key=True)
    created_at = models.DateTimeField(default=datetime.now())