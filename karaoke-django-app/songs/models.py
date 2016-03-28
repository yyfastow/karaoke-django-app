from django.db import models

# Write your models here
class Performer(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Song(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    length = models.IntegerField(default=0)
    performer = models.ForeignKey(Performer)

    def __str__(self):
        return "{} by {}".format(self.title, self.artist)
    
    