from django.db import models

# Create your models here.


class Anime(models.Model):
    name = models.CharField(max_length=500)
    genre = models.CharField(max_length=500)
    type = models.CharField(max_length=50)
    episodes = models.IntegerField()
    rating = models.DecimalField(max_digits=5, decimal_places=2)
    members = models.IntegerField()

    def __str__(self):
        return self.name
