from django.shortcuts import render
from django.http import HttpResponse


def users(request):
    return render(request, 'users/users.html')
