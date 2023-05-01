from django.db import models
from django.contrib.auth.models import User

class hackathonsModel(models.Model):
    title = models.CharField(max_length=50)
    tagline = models.CharField(max_length = 100)
    description = models.CharField(max_length=500)
    hackathon_image = models.ImageField(upload_to='images/')
    type_of_submission = models.CharField(max_length=50)
    startdatetime = models.DateField()
    enddatetime = models.DateField()
    reward_prize = models.IntegerField()
    oragniser = models.CharField(max_length=50)
    githubrepolink = models.CharField(max_length=1000)
    otherlinks = models.CharField(max_length=1000)
    


    class meta:
     verbose_name_plural="1. Hackathons"

class hackersModel(models.Model):
    name = models.CharField(max_length=500)
    hackerid = models.ForeignKey(User, on_delete=models.CASCADE)
    enrolled_hackathons = models.ManyToManyField(hackathonsModel, blank=True)
    class meta:
     verbose_name_plural="2. Hackers"

class submissionModel(models.Model):
    name = models.CharField(max_length=200)
    summary = models.CharField(max_length=500)
    hkr = models.ForeignKey(hackersModel, on_delete=models.CASCADE)
    hkthn = models.ForeignKey(hackathonsModel, on_delete=models.CASCADE)
    submission_link = models.CharField(max_length=1000, blank=True, default='')
    submission_file = models.FileField(upload_to='images/', blank=True, default='')

    class meta:
     verbose_name_plural="3. Submissions"
    
