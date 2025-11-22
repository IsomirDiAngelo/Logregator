from django.db import models
from .api_token import APIToken

class Collector(models.Model):
    name = models.CharField(max_length=10)
    api_token = models.ForeignKey(APIToken, on_delete=models.CASCADE)
    created_at = models.DateTimeField