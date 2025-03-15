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
import password
from password.forms import PassGenForm


# Create your views here.
@login_required(login_url="login")
@login_required(login_url='login')
def homepage(request):
    return render(request, "html/homepage.html")

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
            available_characters = string.ascii_letters + string.digits

            if form.cleaned_data['include_symbols']:
                available_characters += string.punctuation

            if not form.cleaned_data['include_similar_characters']:
                ambiguous_characters = 'lI1O0Z2S5'  # Ambiguous characters to be excluded
                available_characters = re.sub('|'.join(ambiguous_characters), '', available_characters)

            password = ''.join(random.choice(available_characters) for i in range(form.cleaned_data['length']))
        return render(request, 'html/password/password.html', {'password': password})
