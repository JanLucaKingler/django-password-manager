import random
import re
import string

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from password.forms import PassGenForm
from .forms import PasswordForm
from .models import PasswordEntry


@login_required(login_url='login')
def homepage(request):
    """
   Verarbeitet das Rendering der Homepage-Ansicht für authentifizierte Benutzer. Diese Ansicht stellt sicher,
   dass nur eingeloggte Benutzer mit gültigen Sitzungen auf die Homepage zugreifen und mit dem Template interagieren können.
   Ein nicht authentifizierter Benutzer, der versucht, auf diese Ansicht zuzugreifen, wird zur Login-Seite weitergeleitet.

   :param request: Das HTTP-Anforderungsobjekt, das Metadaten über die durchgeführte HTTP-Aktion enthält.
   :type request: HttpRequest
   :return: Ein HttpResponse-Objekt, das das gerenderte Homepage-Template enthält.
   :rtype: HttpResponse
   """
    return render(request, "html/homepage.html")


def logout_page(request):
    """
       Verarbeitet das Ausloggen des Benutzers. Diese Ansicht beendet die Sitzung des aktuell
       angemeldeten Benutzers und leitet ihn anschließend auf die Login-Seite weiter.

       :param request: Das HTTP-Anforderungsobjekt, das Metadaten über die durchgeführte HTTP-Aktion enthält.
       :type request: HttpRequest
       :return: Eine HttpResponse-Umleitung zur Login-Seite.
       :rtype: HttpResponse
       """
    logout(request)
    return redirect('login')


def password_manager(request):
    """
    Verarbeitet die Anzeige und Erstellung von Passwort-Einträgen für den aktuell angemeldeten Benutzer.

    Wenn die Anfrage ein POST-Request ist, wird das Formular mit den übermittelten Daten verarbeitet.
    Bei einem gültigen Formular wird ein neuer Passwort-Eintrag erstellt und mit dem aktuell angemeldeten Benutzer verknüpft.
    Anschließend wird der Benutzer zur Passwort-Verwaltungsseite weitergeleitet.

    Bei einem GET-Request wird ein leeres Formular angezeigt.

    :param request: Das HTTP-Anforderungsobjekt, das Metadaten über die durchgeführte HTTP-Aktion enthält.
    :type request: HttpRequest
    :return: Eine HttpResponse mit der gerenderten Passwort-Verwaltungsseite.
    :rtype: HttpResponse
    """
    if request.method == "POST":
        form = PasswordForm(request.POST)
        if form.is_valid():
            password_entry = form.save(commit=False)
            password_entry.user = request.user
            password_entry.save()
            return redirect('password_manager')

    else:
        form = PasswordForm()

    passwords = PasswordEntry.objects.filter(user=request.user)

    return render(request, "html/password/passwordmanager.html", {'passwords': passwords, 'form': form})


def delete_password(request, password_id):
    """
        Löscht einen Passwort-Eintrag basierend auf der übergebenen ID.

        Diese Methode sucht nach einem Passwort-Eintrag mit der angegebenen ID und löscht ihn aus der Datenbank.
        Nach dem Löschen wird der Benutzer zur Passwort-Verwaltungsseite weitergeleitet.

        :param request:  Die HTTP-Anforderung.
        :param password_id: Die ID des Passwort-Eintrags, der gelöscht werden soll.
        :type password_id: int
        :return: Eine HttpResponse-Umleitung zur Passwort-Verwaltungsseite.
        :rtype: HttpResponse
        """
    password_entry = PasswordEntry.objects.filter(id=password_id, user=request.user).first()

    if password_entry:
        password_entry.delete()

    return redirect('password_manager')


class PasswordGeneratorView(View):
    """
    Eine View, die die Passwort-Generierung für den Benutzer ermöglicht.

    Diese View stellt ein Formular zur Verfügung, mit dem der Benutzer ein Passwort generieren kann.
    Der Benutzer kann angeben, wie lang das Passwort sein soll, ob Sonderzeichen und/oder ähnliche Zeichen enthalten sein sollen.
    Bei einer GET-Anfrage wird das Formular angezeigt, bei einer POST-Anfrage wird das Passwort generiert und dem Benutzer angezeigt.

    Methoden:
    --------
    get(request):
        - Zeigt das Formular zur Passwort-Generierung an.

    post(request):
        - Verarbeitet das Formular, generiert das Passwort basierend auf den Benutzereingaben und zeigt das generierte Passwort an.
    """

    def get(self, request):

        """
        Verarbeitet die GET-Anfrage und zeigt das Formular zur Passwort-Generierung an
        :param request: Das HTTP-Anforderungsobjekt.
        :type request: HttpRequest
        :return: Ein HttpResponse-Objekt, das das Formular zur Passwort-Generierung rendert.
        :rtype: HttpResponse
        """
        form = PassGenForm()

        context = {'form': form}
        return render(request, 'html/password/passwordgenerator.html', context)

    def post(self, request):
        """
        Verarbeitet die POST-Anfrage, um das Passwort basierend auf den Eingabedaten zu generieren,
        Diese Methode verwendet die Daten aus dem Formular, um ein zufälliges Passwort zu erstellen.
        Die Passwort-Optionen (Länge, Sonderzeichen, ähnliche Zeichen) werden aus den Formularfeldern gelesen
        :param request: Das HTTP-Anforderungsobjekt mit den übermittelten Formulardaten.
        :type request: HttpRequest
        :return: Ein HttpResponse-Objekt, das das generierte Passwort anzeigt.
        :rtype: HttpResponse
        """

        password = ""
        form = PassGenForm(request.POST)

        if form.is_valid():
            available_characters = string.ascii_letters + string.digits

            if form.cleaned_data['include_symbols']:
                available_characters += string.punctuation

            if not form.cleaned_data['include_similar_characters']:
                ambiguous_characters = 'lI1O0Z2S5'
                available_characters = re.sub('|'.join(ambiguous_characters), '', available_characters)

            password = ''.join(random.choice(available_characters) for _ in range(form.cleaned_data['length']))
        return render(request, 'html/password/password.html', {'password': password})
