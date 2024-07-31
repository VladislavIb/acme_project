"""Learn forms."""
from django import forms

from .models import Birthday


class BirthdayForm(forms.ModelForm):
    """Birthday form."""

    class Meta:
        """Birthday form meta."""

        model = Birthday
        fields = '__all__'
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'}),
        }
