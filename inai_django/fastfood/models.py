from django.db import models

class Order(models.Model):
    FOOD_CHOISES = (
        ('HAMBURGER', "HAMBURGER"),
        ("PIZZA", "PIZZA"),
        ('CHICKEN ROLS', "CHICKEN ROLS"),
        ('DONNER', "DONNER"),
        ('RAMEN', "RAMEN"),
        ('POTATOES FREE', 'POTATOES FREE'),
        ('SANDWITCH', "SANDWITCH")

    )
    FAST_FOOD_CHOISES = (
        ('OAZIS', 'OAZIS'),
        ("BIR EKI", "BIR EKI"),
        ("IMPERIA PIZZA", "IMPERIA PIZZA"),
        ('EKIDOS', 'EKIDOS'),
        ("PAPAJOHNS", 'PAPAJOHNS'),
        ('DODOPIZZA', 'DODOPIZZA'),
        ("KFC", "KFC")
    )


    title_fast_food = models.CharField(choices= FAST_FOOD_CHOISES, max_length=100)
    quatity_food = models.IntegerField(null=True)
    name = models.CharField(max_length=100)
    number_phone = models.CharField(max_length=13)
    address = models.CharField(max_length=60)
    choise_food = models.CharField(choices=FOOD_CHOISES, max_length=100)