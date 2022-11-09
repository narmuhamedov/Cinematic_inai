from django.db import models

class Poster(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class About_us(models.Model):
    description = models.TextField()
    textssssssss = models.TextField(null=True)
    text2 = models.TextField(null=True)


class Contacts(models.Model):
    name = models.CharField(max_length=50, null=True)
    work = models.CharField(max_length=40, null=True)
    image = models.ImageField(upload_to='')
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()


class Firma(models.Model):
    title = models.CharField(max_length=100)
    total_cost = models.IntegerField()
    image = models.ImageField(upload_to='')
    email = models.EmailField()
    date_register = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title