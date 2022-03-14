from django.db import models
 
# Create your models here.


class Information(models.Model):

    name=models.CharField(max_length=264)
    email=models.EmailField(max_length=264)
    profile_pic=models.ImageField(upload_to='img')


    def __str__(self):
        return self.name
