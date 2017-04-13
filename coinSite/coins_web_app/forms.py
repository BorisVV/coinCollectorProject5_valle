from django import forms
from .models import DisplayQuaters

class NewQuatersForm(forms.ModelForm):
    class Meta:
        model = DisplayQuaters
        fields = ('number', 'state', 'release_date', 'elements', 'engraver', 'link')
