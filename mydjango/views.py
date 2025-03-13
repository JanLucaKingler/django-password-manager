import string
import re
import random
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views import View
from .forms import PassGenForm
import mydjango
from mydjango.forms import PassGenForm


# Create your views here.
@login_required(login_url="login")
@login_required(login_url='login')
def home_page(request):
    return render(request, "html/homepage.html")


def sign_up_page(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            return HttpResponse("Die Passwörter stimmen nicht überein")
        else:
            my_user = User.objects.create_user(uname, email, password1)
            my_user.save()
        return redirect('login')

    return render(request, 'html/login/signup.html')


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Benutzername oder Password ist Falsch")
    return render(request, 'html/login/login.html')


def logout_page(request):
    logout(request)
    return redirect('login')


def password_manager(request):
    return render(request, "html/password/passwordmanager.html")


def overview(request):
    return render(request, "html/button.html")


class Index(View):
    def get(self, request):
        form = PassGenForm()

        context = {'form': form}
        return render(request, 'html/password/passwordgenerator.html', context)

    def post(self, request):

        form = PassGenForm(request.POST)

        if form.is_valid():
            available_charaters = string.ascii_letters + string.digits

            if form.cleaned_data['include_symbols']:
                available_charaters += string.punctuation

            if not form.cleaned_data['include_similar_characters']:
                ambiguous_characters = 'lI1O0Z2S5'  # Ambiguous characters to be excluded
                available_charaters = re.sub('|'.join(ambiguous_characters), '', available_charaters)

            password = ''.join(random.choice(available_charaters) for i in range(form.cleaned_data['length']))
        return render(request, 'html/password/password.html', {'password': password})
