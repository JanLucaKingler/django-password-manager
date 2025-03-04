from django import  forms
from django.forms.widgets import NumberInput


class RangeInput(NumberInput):
    input_type = 'range'

class PassGenForm(forms.Form):
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