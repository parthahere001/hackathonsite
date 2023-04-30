from django.db import models
from django.contrib.auth.models import User

class hackathonsModel(models.Model):
    title = models.CharField(max_length=50)
    tagline = models.CharField(max_length = 100)
    description = models.CharField(max_length=500)
    background_image = models.ImageField(upload_to='images/')
    hackathon_image = models.ImageField(upload_to='images/')
    type_of_submission = models.CharField(max_length=50)
    startdatetime = models.DateTimeField()
    enddatetime = models.DateTimeField()
    reward_prize = models.IntegerField()
    oragniser = models.CharField(max_length=50)
    


    class meta:
     verbose_name_plural="1. Hackathons"

class hackersModel(models.Model):
    name = models.CharField(max_length=500)
    hackerid = models.ForeignKey(User, on_delete=models.CASCADE)
    enrolled_hackathons = models.ManyToManyField(hackathonsModel, blank=True, default='')
    class meta:
     verbose_name_plural="2. Hackers"
