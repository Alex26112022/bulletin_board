from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

options = {'blank': True, 'null': True}


class User(AbstractUser):
    """ Модель пользователя. """
    user_role = (
        ('user', 'Пользователь'),
        ('admin', 'Администратор')
    )
    username = None
    email = models.EmailField(unique=True, db_index=True,
                              verbose_name='E-mail',
                              help_text='Укажите E-mail')
    phone = PhoneNumberField(region='RU', verbose_name='Телефон',
                             help_text='Укажите телефон', **options)
    role = models.CharField(max_length=10, choices=user_role,
                            verbose_name='Роль', default='user',
                            help_text='Укажите роль пользователя')
    image = models.ImageField(upload_to='users/image', verbose_name='Аватар',
                              help_text='Загрузите аватар', **options)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email
