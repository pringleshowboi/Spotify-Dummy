from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User

# Create your views here.
def user_login(request):
    return render(request, 'authentication/login.html')

def authenticate_user(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('spotify_homepage_dummy:home'))
    else:
        messages.error(request, "Invalid username or password!")
        return HttpResponseRedirect(reverse('user_auth:login'))

def register(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        if User.objects.filter(username=username).exists():
            error_message = 'Username is already taken.'
            return render(request, 'authentication/register.html', {'WARNING': error_message})
        user = User.objects.create_user(username=username, password=password)
        user.save()
        return redirect('spotify_homepage_dummy:home')
    else:
        return render(request, 'authentication/register.html')
