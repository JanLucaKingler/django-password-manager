from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


# Create your views here.


def SignUpPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        password = request.POST.get('password')


        my_user = User.objects.create_user(uname,password)
        my_user.save()
        return redirect('login')


    return render(request, 'signup.html')


def LoginPage(request):
    if  request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('pass')
    return render(request, 'login.html')
