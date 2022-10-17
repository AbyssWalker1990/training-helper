from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name="main_page"), # in main templates
    # Rework with pk later
    path('trainings/<str:pk>', views.all_user_trainings, name="all-user-trainings"),
    path('training-single/<str:pk>', views.user_single_training, name="training-single"),
    path('create-training', views.create_training, name="create-training"),
    path('create-exercise/<str:pk>', views.create_exercise, name="create-exercise"),
    path('create-set/<str:pk>', views.create_set, name="create-set"),

]
