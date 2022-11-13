from django import forms
from . import models

class ClothingForm(forms.ModelForm):
    class Meta:
        model = models.ManClothing
        fields = '__all__'