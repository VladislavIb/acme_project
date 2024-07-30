"""Birthday model."""
from django.db import models


class Birthday(models.Model):
    """Birthday model."""

    first_name: models.CharField = models.CharField('Имя', max_length=20)
    last_name: models.CharField = models.CharField(
        'Фамилия', blank=True, help_text='Необязательное поле', max_length=20
    )
    birthday: models.DateField = models.DateField('Дата рождения')
