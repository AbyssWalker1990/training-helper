from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Training, Exercise, Set
from django.contrib.auth.models import User
from .forms import TrainingForm
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

@login_required(login_url="login")
def create_training(request):
    profile = request.user # тут ми зберігаємо профіль, декортаор не дасть нам це робити незалогіненим
    form = TrainingForm()

    if request.method == 'POST':
        print('Triggered')
        form = TrainingForm(request.POST)
        if form.is_valid():
            training = form.save(commit=False) # Не застосовуємо зміни до дб, а поки що тільки записуємо у змінну
            training.user = profile # Редагуємо поле власника використовуючи інфу з профіля
            training.save()  # І тільки тепер зберігаємо
            return redirect(f"training-single/{training.id}")

    context = {'form': form}
    return render(request, "training_diary/create-training-form.html", context)
