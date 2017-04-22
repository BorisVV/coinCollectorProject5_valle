from django import forms
from .models import DisplayQuarters

class NewQuartersForm(forms.ModelForm):
    class Meta:
        model = DisplayQuarters
        fields = ('number', 'state', 'release_date', 'elements', 'engraver', 'image_link')
