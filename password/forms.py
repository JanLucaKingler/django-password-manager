from django import forms
from django.forms.widgets import NumberInput

from password.models import PasswordEntry


class RangeInput(NumberInput):
    """
        Anpassung des NumberInput-Widgets für einen Range-Slider.

        Attribute:
        ----------
        input_type : str
            legt den HTML-Eingabetyp auf 'range' fest, um einen Schieberegler zu erstellen.

        Verwendung:
        -----------
        Wird in Formularfeldern genutzt, um numerische Werte über einen Slider auszuwählen.
        """

    input_type = 'range'


class PassGenForm(forms.Form):
    """
       Formular zur Konfiguration der Passwortgenerierung.

       Felder:
       -------
       length: IntegerField
           - Bezeichnet die Länge des zu generierenden Passworts.
           - Erforderlich: Ja.
           - Verwendet ein benutzerdefiniertes RangeInput-Widget mit Min- und Max-Werten (1 bis 64).

       include_symbols : BooleanField
           - Gibt an, ob Symbole (z. B. @, &, $ und !) im Passwort enthalten sein sollen.
           - Erforderlich: Nein (Optional).

       include_similar_characters : BooleanField
           - Gibt an, ob ähnliche Zeichen (z. B. 0, O, l, 1) vermieden werden sollen.
           - Erforderlich: Nein (Optional).

       Hinweise:
       ---------
       - Dieses Formular wird verwendet, um die Eingaben des Nutzers für die
         Passwortgenerierung zu erfassen.
       - Anpassung der Widgets erfolgt über `attrs`, um CSS-Klassen und IDs für das Styling zu setzen.
       """
    length = forms.IntegerField(
        label='Password length',
        required=True,
        widget=RangeInput(attrs={'min': '1', 'max': '64', 'class': 'range', 'id': 'lengthRangeInput'}))

    include_symbols = forms.BooleanField(
        label='Include symbols (@&$!#?)',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'checkboxInout'}))

    include_similar_characters = forms.BooleanField(
        label='Include symbols (e.g. 00 l1 Z2)',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'checkboxInout'}))

    def clean_length(self):
        """
        Validiert die Passwortlänge.
        """
        length = self.cleaned_data.get('length')
        if length < 1 or length > 64:
            raise forms.ValidationError('Die Passwortlänge muss zwischen 1 und 64 liegen.')
        return length


class PasswordForm(forms.ModelForm):
    """
       Formular zur Verwaltung von Passwort-Einträgen (ModelForm).

       Verwendung:
       -----------
       - Erzeugt ein Formular basierend auf dem `PasswordEntry`-Modell.
       - Ermöglicht das Erfassen von:
           1. site_name: Der Name der Website oder Anwendung.
           2. password: Das generierte oder gespeicherte Passwort.

       Meta-Klasse:
       ------------
       model: PasswordEntry
           Referenziert das `PasswordEntry`-Modell.
       fields: list
           begrenzt die Felder auf "site_name" und "password".
       """

    class Meta:
        """
        Die Meta-Klasse enthält die Konfigurationen und Optionen für das Model, das mit diesem Formular verbunden ist.

        In diesem Fall gibt die Meta-Klasse an, dass das Formular mit dem `PasswordEntry`-Model verbunden ist und legt fest,
        welche Felder des Models im Formular verwendet werden sollen.

        Attribute:
        ----------
        model: class
            Das Model, mit dem dieses Formular verbunden ist. In diesem Fall ist es das `PasswordEntry`-Model,
            welches die Datenbanktabelle für Passwort-Einträge darstellt.

        fields: list
            Eine Liste von Feldern, die aus dem `PasswordEntry`-Model im Formular verwendet werden sollen.
            In diesem Fall sind dies die Felder "site_name" und "password", die im Formular angezeigt und bearbeitet werden können.
        """
        model = PasswordEntry
        fields = ["site_name", "password"]
