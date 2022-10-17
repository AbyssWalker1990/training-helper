from django.forms import ModelForm
from django import forms
from .models import Training


class TrainingForm(ModelForm):
    class Meta:
        model = Training
        fields = ['name', 'description', 'date']
