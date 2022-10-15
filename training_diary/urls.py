from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name="main_page"), # in main templates
    # Rework with pk later
    path('trainings', views.all_user_trainings, name="all-user-trainings"),
    path('training-single', views.user_single_training, name="training-single")

]
