"""Learn forms."""
from django import forms

from django.core.exceptions import ValidationError
from django.core.mail import send_mail

from .models import Birthday, Congratulation

BEATLES = {'Джон Леннон', 'Пол Маккартни', 'Джордж Харрисон', 'Ринго Старр'}


class BirthdayForm(forms.ModelForm):
    """Birthday form."""

    class Meta:
        """Birthday form meta."""

        model = Birthday
        exclude = ('authour',)
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_first_name(self):
        """Clean first name."""
        first_name = self.cleaned_data['first_name']
        return first_name.split()[0]

    def clean(self):
        """Clean data."""
        super().clean()
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']

        if f'{first_name} {last_name}' in BEATLES:
            send_mail(
                subject='Another Beatles member',
                message=(
                    f'{first_name} {last_name} пытался опубликовать запись!'
                ),
                from_email='birthday_form@acme.not',
                recipient_list=['admin@acme.not'],
                fail_silently=True,
            )
            raise ValidationError(
                'Мы тоже любим Битлз, но введите, пожалуйста, настоящее имя!'
            )


class CongratulationForm(forms.ModelForm):
    """Congratulation form."""

    class Meta:
        """Congratulation form meta."""

        model = Congratulation
        fields = ('text',)
