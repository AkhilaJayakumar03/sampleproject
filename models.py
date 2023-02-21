from django.db import models

# Create your models here.

class regmodel(models.Model):
    username = models.CharField(max_length=30)
    email =models.EmailField()
    phone = models.IntegerField()
    password = models.CharField(max_length=20)


class empmode(models.Model):
    employee_name=models.CharField(max_length=30)
    employee_id=models.IntegerField()
    company_name=models.CharField(max_length=30)
    email=models.EmailField()
    department=models.CharField(max_length=30)


class imgmodel(models.Model):
    imgname=models.CharField(max_length=30)
    imgfile=models.ImageField(upload_to='sampleapp/static')


class audiomodel(models.Model):
    audname=models.CharField(max_length=40)
    audimg=models.ImageField(upload_to='sampleapp/static')
    audfile=models.FileField(upload_to='sampleapp/static')


class videomodel(models.Model):
    videoname=models.CharField(max_length=30)
    videofile=models.FileField(upload_to='sampleapp/static')