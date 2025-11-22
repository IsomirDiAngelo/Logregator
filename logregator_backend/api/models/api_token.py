from django.db import models

class APIToken(models.Model):
    content = models.CharField
    created_at = models.DateTimeField
    updated_at = models.DateTimeField