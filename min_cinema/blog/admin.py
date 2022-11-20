from django.contrib import admin
from . import models

admin.site.register(models.Poster)
admin.site.register(models.Film)
admin.site.register(models.Food)