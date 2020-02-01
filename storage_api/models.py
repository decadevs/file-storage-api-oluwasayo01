from django.db import models

class Bucket(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
