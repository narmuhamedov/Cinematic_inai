from django.db import models

class Poster(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class About_us(models.Model):
    image = models.ImageField(upload_to='')
    description = models.TextField()