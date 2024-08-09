"""Birthday model."""
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

from .validators import real_age


User = get_user_model()


class Birthday(models.Model):
    """Birthday model."""

    first_name: models.CharField = models.CharField('Имя', max_length=20)
    last_name: models.CharField = models.CharField(
        'Фамилия', blank=True, help_text='Необязательное поле', max_length=20
    )
    birthday: models.DateField = models.DateField(
        'Дата рождения', validators=(real_age,)
    )
    image = models.ImageField('Фото', upload_to='birthdays_images', blank=True)
    author: models.ForeignKey = models.ForeignKey(
        User, verbose_name='Автор записи', on_delete=models.CASCADE, null=True
    )

    class Meta:
        """Birthday model meta."""

        constraints = (
            models.UniqueConstraint(
                fields=('first_name', 'last_name', 'birthday'),
                name='Unique person constraint'
            ),
        )

    def get_absolute_url(self):
        """Get absolute url."""
        return reverse('birthday:detail', kwargs={"pk": self.pk})
