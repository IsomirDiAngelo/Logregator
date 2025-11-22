from datetime import datetime
from django.db import models

class APIToken(models.Model):
    content = models.CharField(null=True)
    created_at = models.DateTimeField(default=datetime.now())
    updated_at = models.DateTimeField(default=datetime.now())