
from django import forms

class FavoriteEventForm(forms.Form):
    event_id = forms.IntegerField(widget=forms.HiddenInput)