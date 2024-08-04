from django.db import models
from musician.models import Musician

class Album(models.Model):
    name = models.CharField(max_length=255)
    release_date = models.DateField()
    choices = (('1','1'),('2','2'),('3','3'),('4','4'),('5','5'))
    rating = models.CharField(max_length=5,choices=choices)
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE, related_name='albums')

    def __str__(self):
        return self.name
