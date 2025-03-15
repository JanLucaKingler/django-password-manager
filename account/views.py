from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages


def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Ungültiger Benutzername oder Passwort')
    return render(request, 'html/login/login.html')


def sign_up_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Benutzername existiert bereits')
        else:
            User.objects.create_user(username=username, password=password)
            messages.success(request, 'Benutzer erfolgreich erstellt. Du kannst dich jetzt einloggen.')
            return redirect('login_page')
    return render(request, 'html/login/signup.html')
