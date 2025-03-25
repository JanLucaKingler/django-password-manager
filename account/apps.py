from django.apps import AppConfig


class AccountConfig(AppConfig):
    """
        Konfiguration der Django-Anwendung 'account'.

        Diese Klasse erbt von `AppConfig` und stellt die Konfiguration für die 'account'-App innerhalb des Django-Projekts bereit.
        Die Konfiguration definiert die grundlegenden Einstellungen für das Modell der Anwendung sowie das Verzeichnis, in dem sich die App befindet.
        Die `default_auto_field`-Einstellung legt den Standard-Typ für automatisch generierte Felder fest, der in der 'account'-App verwendet wird.

        Attribute:
        ----------
        default_auto_field : str
            Der Typ des automatisch generierten Primärschlüssels für alle Modelle in dieser Anwendung.
            Standardmäßig wird `BigAutoField` verwendet, was ein `BigIntegerField` mit automatisch inkrementiertem Wert ist.

        name: str
            Der Name der Anwendung. In diesem Fall ist es 'account', was dem Verzeichnisnamen der Anwendung entspricht.
        """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'account'
