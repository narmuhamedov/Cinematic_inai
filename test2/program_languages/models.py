from django.db import models

class ProgLang(models.Model):
    COUNTRIES = (
        ('KYRGYZSTAN', "KYRGYZSTAN"),
        ('GERMANY', 'GERMANY'),
        ("USA", "USA"),
        ('RUSSIA', "RUSSIA"),
        ("INDIA", "INDIA"),
        ('JAPAN', 'JAPAN')
    )

    name_lang = models.CharField(max_length=60)
    description_lang = models.TextField()
    image = models.ImageField(upload_to='')
    popular_lang_in_countries = models.CharField(max_length=60, choices=COUNTRIES)