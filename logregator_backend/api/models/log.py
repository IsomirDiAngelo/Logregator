from django.db import models
from .collector import Collector

class Log(models.Model):
    raw_content = models.JSONField(null=True)
    collector = models.ForeignKey(Collector, default=None, on_delete=models.CASCADE)