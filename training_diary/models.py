from django.db import models
from django.contrib.auth.models import User
import uuid
from datetime import date

# Create your models here.



class Training(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    description = models.CharField(max_length=800, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True, default=date.today().strftime("%Y-%m-%d"))

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)


class Exercise(models.Model):
    exercise_name = models.CharField(max_length=150)
    training = models.ForeignKey(Training, on_delete=models.CASCADE)
    number_of_sets = models.IntegerField(blank=True, null=True)
    reps = models.IntegerField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.exercise_name)

class Set(models.Model):
    reps = models.IntegerField()
    weight = models.FloatField()
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return f"{self.reps}*{self.weight}"

