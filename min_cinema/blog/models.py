from django.db import models


class Poster(models.Model):
    title = models.CharField(max_length=100)
    month = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    education = models.CharField(max_length=20)
    image = models.ImageField(upload_to='')
    description = models.TextField()

    def __str__(self):
        return self.title


class Film(models.Model):
    url_film = models.URLField(null=True)

    def __str__(self):
        return self.url_film


class Food(models.Model):
    title_food = models.CharField(max_length=60)
    gram_food = models.IntegerField()
    cost_food = models.IntegerField()

    def __str__(self):
        return self.title_food

