from django.urls import path
from . import views


urlpatterns = [
    path('profiles/', views.users, name="profiles"),
    # path('user/<str:pk>', views.users, name="user"),
]
