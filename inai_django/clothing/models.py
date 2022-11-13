from django.db import models

class ManClothing(models.Model):
    TYPE_CLOTHING = (
        ('Jeans', 'Jeans'),
        ('T-Shirt', 'T-Shirt'),
        ('Houdey', 'Houdey'),
        ('Pullower', 'Pullower'),
        ('Suit', 'Suit')
    )

    title = models.CharField(max_length=60)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='')
    type_clothing = models.CharField(max_length=60, choices=TYPE_CLOTHING)

    def __str__(self):
        return self.title