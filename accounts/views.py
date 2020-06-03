from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User


def register(request):
    if (request.method == 'POST'):
        # register user
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password != password2:
            messages.error(request, "Passwords don't match!")
            return redirect('register')
        elif User.objects.filter(username=username).exists():
            messages.error(request, "There's already a user with this username")
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.error(request, "There's already a user with this email address")
            return redirect('register')
        else:
            # create the user
            user = User.objects.create_user(
                username=username, password=password, email=email, first_name=first_name, last_name=last_name)

            # login
            auth.login(request, user)
            messages.success(request, 'You have been logged in.')
            return redirect('index')
    else:
        return render(request, 'accounts/register.html')


def login(request):
    if (request.method == 'POST'):
        # login user
        return
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    return redirect('index')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')
