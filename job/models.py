from django.db import models
from .images_urls import *

# Create your models here.


JOB_TYPE = (
    ('Full time', 'Full time'),
    ('Part time', 'Part time'),

)


class Job(models.Model):
    title = models.CharField(max_length=100)
    # location
    job_type = models.CharField(max_length=15, choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to=get_job, blank=True, null=True, max_length=90000)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=25)
    published_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
