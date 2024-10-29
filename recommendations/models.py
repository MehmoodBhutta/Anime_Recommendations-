from django.db import models

class Anime(models.Model):
    anime_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=255)
    genre = models.TextField()
    type = models.CharField(max_length=50)
    episodes = models.IntegerField(null=True)
    rating = models.FloatField()
    members = models.IntegerField()

    def __str__(self):
        return self.name