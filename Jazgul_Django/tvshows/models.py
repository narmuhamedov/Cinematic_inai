from django.db import models

class TvShow(models.Model):
    GENRE = (
        ('DETECTIVE', 'DETECTIVE'),
        ('HORROR', 'HORROR'),
        ('ANIME', 'ANIME'),
        ('MELODRAMA', 'MELODRAMA'),
        ('FAIRYTAILES', 'FAIRYTAIL')
    )

    title = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    genre = models.CharField(choices=GENRE, max_length=100)
    quantity = models.IntegerField()
    trailer = models.URLField()

    def __str__(self):
        return self.title