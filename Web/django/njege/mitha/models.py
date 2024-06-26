from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=25,blank=False,null=False)
    email = models.EmailField()
    phone = models.IntegerField()
    age = models.IntegerField()
    image = models.ImageField(upload_to='uploads/images', default="clock.png")

    def __str__(self) :
        return self.name
