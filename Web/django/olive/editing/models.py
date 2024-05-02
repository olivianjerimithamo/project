from django.db import models
# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=20, blank=False)
    phone = models.IntegerField(blank=False)
    email = models.EmailField(blank=False)
    image = models.ImageField(upload_to='images/', blank=False, default="default.jpg")


    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=15, blank=False)
    age = models.IntegerField(blank=False)
    phone = models.IntegerField(blank=False)
