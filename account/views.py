from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages

def login_page(request):
    """
    Handles user login by verifying the provided username and password against the
    authenticated users in the system. If the authentication succeeds, the user is
    logged in, and they are redirected to the home page. Otherwise, an error
    message is displayed.

    :param request: A Django HttpRequest object containing the request information
        such as method, POST data, and session.
    :type request: HttpRequest

    :return: A rendered login page template when the method is not POST or the
        authentication fails. If authentication is successful, it redirects the
        user to the home page.
    :rtype: HttpResponse or HttpResponseRedirect
    """
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
    """
    Displays the sign-up page and handles the user registration process. If the
    request method is POST, it attempts to create a new user account. If the user
    already exists, it displays an error message. Upon successful registration,
    an informational message is shown and the user is redirected to the login page.

    :param request: The HTTP request object containing metadata about the request
            and user inputs from the sign-up form.
    :type request: HttpRequest
    :return: The rendered sign-up page if the request method is not POST, or a
            redirect to the login page upon successful registration.
    :rtype: HttpResponse
    """
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
