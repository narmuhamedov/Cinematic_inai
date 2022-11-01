from django.db import models



class Cars(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    color = models.CharField(max_length=60)
    created_year = models.DateField()
    ratings = models.IntegerField(max_length=10, null=True)

    def __str__(self):
        return self.title


class About(models.Model):
    name = models.CharField(max_length=50)
    job = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    site = models.URLField()

    def __str__(self):
        return self.name