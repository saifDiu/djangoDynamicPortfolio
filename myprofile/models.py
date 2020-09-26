from django.db import models
from PIL import Image
from django.utils import *

class myProfile(models.Model):
    uname = models.CharField(max_length=200, null=True)
    utitle = models.CharField(max_length=200, null=True)
    age = models.IntegerField(null=True, default=0)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=200, null=True)
    adress = models.CharField(max_length=200, null=True)
    language = models.CharField(max_length=200, null=True)
    about = models.TextField(null=True)
    profile_pics = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.uname


class worksarea(models.Model):
    myProfile = models.ForeignKey(myProfile, on_delete=models.CASCADE)
    planguage = models.CharField(max_length=50, null=True)
    frameworkname = models.CharField(max_length=100, null=True)
    workTitle = models.CharField(max_length=200, null=True)
    workDescription = models.TextField(null=True)


    def __str__(self):
        return self.workTitle



class projects(models.Model):
    myProfile = models.ForeignKey(myProfile, on_delete=models.CASCADE)
    projectName = models.CharField(max_length=200, null=True)
    projectTools = models.CharField(max_length=200, null=True)
    projectDescription = models.TextField(null=True)
    projectImage = models.ImageField(null=True, blank=True)


    def __str__(self):
        return self.projectName



class education(models.Model):
    myProfile = models.ForeignKey(myProfile, on_delete=models.CASCADE)
    degree = models.CharField(max_length=200, null=True)
    degreeTitle = models.CharField(max_length=200, null=True)
    institution = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    yearDuration = models.CharField(max_length=100, null=True, blank=True)
    result = models.FloatField(null=True)

    def __str__(self):
        return self.degreeTitle
