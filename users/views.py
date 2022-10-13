from django.shortcuts import render
from django.http import HttpResponse
from .models import Profile


def users(request):
    all_users = Profile.objects.all()
    context = {'all_users': all_users}
    return render(request, 'users/users.html', context)


def user_profile(request, pk):
    profile = Profile.objects.get(id=pk)
    context = {'profile': profile}
    return render(request, 'users/user-profile.html', context)