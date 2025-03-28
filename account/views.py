from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages


def login_page(request):
    """
        Verarbeitet den Benutzer-Login.

        - Prüft, ob die Anfrage vom Typ POST ist.
        - Authentifiziert den Benutzer mit Benutzername und Passwort.
        - Bei Erfolg: Anmeldung und Weiterleitung zur 'home'-Seite.
        - Bei Misserfolg: Anzeige einer Fehlermeldung.

        Parameter:
        ----------
        request: HttpRequest
            die HTTP-Anfrage des Benutzers.

        Rückgabewert:
        -------------
        HttpResponse
            - Erfolgreiche Anmeldung: Weiterleitung zur 'home'-Seite.
            - Fehlgeschlagene Anmeldung oder GET-Anfrage: Anzeige der Login-Seite.
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
      Verarbeitet die Benutzerregistrierung.

      - Prüft, ob die Anfrage vom Typ POST ist.
      - Überprüft, ob der Benutzername bereits existiert.
      - Bei vorhandenem Benutzer: Fehlermeldung.
      - Bei neuem Benutzer: Erstellt einen Account und leitet zur Login-Seite weiter.

      Parameter:
      ----------
      request: HttpRequest
          die HTTP-Anfrage des Benutzers.

      Rückgabewert:
      -------------
      HttpResponse
          - Erfolgreiche Registrierung: Weiterleitung zur Login-Seite.
          - Bei Fehlern oder GET-Anfrage: Anzeige des Registrierungsformulars.
      """
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Benutzername existiert bereits')
        else:
            User.objects.create_user(username=username, password=password)
            messages.success(request, 'Benutzer erfolgreich erstellt. Du kannst dich jetzt einloggen.')
            return redirect('login_page')
    return render(request, 'html/login/signup.html')
