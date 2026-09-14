from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=200)
    status = models.CharField(max_length=20, default="pending")
    release_year = models.IntegerField(null=True, blank=True)
    director = models.CharField(max_length=200, blank=True)
    genre = models.CharField(max_length=100, blank=True)
    rating = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
