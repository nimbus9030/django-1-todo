from django.db import models
from django.utils import timezone

# Create your models here.
class Todo(models.Model):
    title = models.CharField( max_length = 100 )
    isCompleted = models.BooleanField(default=False)
    pub_date = models.DateTimeField(default=timezone.now )
