from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=70, blank=False, default='')
    last_name = models.CharField(max_length=70, blank=False, default='')
    password = models.CharField(max_length=70, blank=False, default='')
    email = models.CharField(max_length=70, blank=False, default='')
    country = models.CharField(max_length=70, blank=False, default='')
    city = models.CharField(max_length=70, blank=False, default='')
    job_title = models.CharField(max_length=70, blank=False, default='')
    company = models.CharField(max_length=70, blank=False, default='')
    verified = models.BooleanField(default=False)