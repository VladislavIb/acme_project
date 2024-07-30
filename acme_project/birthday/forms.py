"""Learn forms."""
from django import forms

from .models import Birthday


class BirthdayForm(forms.ModelForm):
    """Birthday form."""

    class Meta:
        model = Birthday
        fields = '__all__'
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'}),
        }
