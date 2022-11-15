from django import forms
from . import models

class ProgLangForms(forms.ModelForm):
    class Meta:
        model = models.ProgLang
        fields = '__all__'