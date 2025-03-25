from django.contrib.auth.models import User
from django.db import models


class PasswordEntry(models.Model):
    """
       Modell zur Speicherung von Passwort-Einträgen für Benutzer.

       Dieses Modell ermöglicht es Benutzern, Passwörter für verschiedene Websites oder Anwendungen zu speichern.
       Es enthält einen Bezug zu einem Benutzer und speichert den Namen der Website und das zugehörige Passwort.

       Felder:
       -------
       user: ForeignKey(User)
           - Verweist auf das `User`-Modell, um zu speichern, welchem Benutzer der Passwort-Eintrag gehört.
           - `on_delete=models.CASCADE` bedeutet, dass alle zugehörigen Passwort-Einträge gelöscht werden, wenn der Benutzer gelöscht wird.

       site_name : CharField
           - Der Name der Website oder Anwendung, für die das Passwort gespeichert wird.
           - Maximale Länge: 255 Zeichen.

       password: CharField
           - Das Passwort für die angegebene Website oder Anwendung.
           - Maximale Länge: 255 Zeichen.

       Methoden:
       --------
       __str__():
           - Gibt den `site_name` als String zurück, um eine lesbare Darstellung des Objekts zu ermöglichen.
       """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    site_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.site_name
