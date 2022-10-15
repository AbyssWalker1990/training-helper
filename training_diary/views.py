from django.shortcuts import render
from .models import Training, Exercise, Set
from django.contrib.auth.models import User
# Create your views here.

def main_page(request):
    return render(request, 'main_page.html')


def all_user_trainings(request, pk): # Need to add pk later
    user = User.objects.get(id=pk)
    print('USER = ', user)
    trainings = Training.objects.filter(user=user)
    context = {'trainings': trainings}
    return render(request, 'training_diary/trainings.html', context)


def user_single_training(request, pk):
    current_training = Training.objects.get(id=pk)
    exercises = current_training.exercise_set.all()
    context = {'exercises': exercises}
    return render(request, 'training_diary/training-single.html', context)
