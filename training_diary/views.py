from django.shortcuts import render

# Create your views here.

def main_page(request):
    return render(request, 'main_page.html')


def all_user_trainings(request): # Need to add pk later
    return render(request, 'training_diary/trainings.html')


def user_single_training(request):
    return render(request, 'training_diary/training-single.html')
