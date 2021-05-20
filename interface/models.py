from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Link(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    meeting_name = models.CharField(max_length=100)
    meeting_link = models.CharField(max_length = 100)

    start_time = models.TimeField(default='08:00:00')
    end_time = models.TimeField(default='17:00:00')

    monday = models.BooleanField(default = False)
    tuesday = models.BooleanField(default = False)
    wednesday = models.BooleanField(default = False)
    thursday = models.BooleanField(default = False)
    friday = models.BooleanField(default = False)
    saturday = models.BooleanField(default = False)
    sunday = models.BooleanField(default = False)

    def __str__(self):
        return self.meeting_name
