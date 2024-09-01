from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Song(models.Model):
    song_id=models.AutoField(primary_key=True)
    name =models.CharField(max_length=2000)
    singer =models.CharField(max_length=2000)
    tags =models.CharField(max_length=2000)
    image =models.ImageField(upload_to='images')
    song =models.FileField(upload_to='images')
    movie =models.CharField(max_length=1000,default="")
    average_rating=models.FloatField(default=0)

    def __str__(self):
        return self.name

class Rating(models.Model):
    user =models.ForeignKey(User,on_delete=models.CASCADE)
    song =models.ForeignKey(Song,on_delete=models.CASCADE)
    rating =models.PositiveIntegerField(choices=[(i,i)for i in range(1,6)])

    class Meta:
        unique_together =('user','song')


class Topsongs(models.Model):
    song_id =models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    singer =models.CharField(max_length=2000)
    tags =models.CharField(max_length=2000)
    image =models.ImageField(upload_to="images")
    song=models.FileField(upload_to="images")
    movie=models.CharField(max_length=1000)


    def __str__(self):
        return self.name

