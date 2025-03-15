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
    """
    Handles the rendering of the homepage view for authenticated users. This view ensures that only
    logged-in users with valid sessions can access and interact with the homepage template. An
    unauthenticated user attempting to access this view will be redirected to the login page.

    :param request: The HTTP request object that includes metadata about the request HTTP action.
    :type request: HttpRequest
    :return: An HttpResponse object containing the rendered homepage template.
    :rtype: HttpResponse
    """
    return render(request, "html/homepage.html")


def logout_page(request):
    """
    Logs out a user from their active session and redirects them to the login page.

    This function handles the logout process for an authenticated user. Upon calling,
    the user is properly logged out, clearing their session data, and then they are
    redirected to the login endpoint, ensuring a clear exit from their current session.

    :param request: The HTTP request object containing metadata about the current request.
                    This is used to identify the user's session and perform the logout process.

    :return: A redirection to the login page, ensuring the user is redirected
             post-logout for further action or re-authentication.
    """
    logout(request)
    return redirect('login')


def password_manager(request):
    """
    Renders the "Password Manager" HTML page.

    This function processes a web request and returns a rendered template
    for the "Password Manager" page. It is typically called as part of
    handling HTTP requests in a web application.

    :param request: HttpRequest object representing the HTTP request.
    :type request: HttpRequest
    :return: HttpResponse object containing the rendered "Password Manager" HTML page.
    :rtype: HttpResponse
    """
    return render(request, "html/password/passwordmanager.html")


def overview(request):
    """
    Renders the overview page with a specified HTML template.

    :param request: The HTTP request object containing metadata about the
        client's request.
    :return: An HTTP response object which includes the rendered HTML
        representation for the "html/button.html" template.
    """
    return render(request, "html/button.html")


class Index(View):
    """
    A Django view class for generating random passwords.

    This class provides a functionality for both rendering a form to generate passwords
    (GET request) and processing the submitted form to create a random password based on
    the selected options (POST request). Users can include/exclude symbols or similar-looking
    characters, and specify the desired password length.

    :ivar template_name_get: The template rendered for the GET request.
    :type template_name_get: str
    :ivar template_name_post: The template rendered for the POST request.
    :type template_name_post: str
    """

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
