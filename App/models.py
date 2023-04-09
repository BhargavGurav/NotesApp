from django.db import models
from django.contrib.auth.models import User 
import datetime

# Create your models here.
class Created(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    note = models.TextField()
    subject = models.CharField(max_length=50)
    created_on = models.DateTimeField()

    def __str__(self):
        return self.user.email

class Uploaded(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    created_on = models.DateTimeField()
    note_file = models.FileField(upload_to='media/uploaded/')

    

