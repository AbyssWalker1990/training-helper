from django.forms import ModelForm
from django import forms
from .models import Training, Exercise, Set


class TrainingForm(ModelForm):
    class Meta:
        model = Training
        fields = ['name', 'description', 'date']


class ExerciseForm(ModelForm):
    class Meta:
        model = Exercise
        fields = ['exercise_name', 'number_of_sets', 'reps', 'weight']


class SetForm(ModelForm):
    class Meta:
        model = Set
        fields = ['reps', 'weight']
