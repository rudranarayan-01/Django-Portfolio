from django.db import models
from django.db.models.base import Model
3
# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=25)
    email=models.EmailField()
    phonenumber=models.CharField(max_length=10)
    description=models.TextField()

    def __str__(self):
        return self.name


class Project(models.Model):
    title=models.CharField(max_length=60)
    description=models.TextField()
    link=models.CharField(max_length=100000000000000, null=True, blank=True)
    img=models.ImageField(upload_to='portfolio',default='DEFAULT VALUE')

    def __str__(self):
        return self.title
