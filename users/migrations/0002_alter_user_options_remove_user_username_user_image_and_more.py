# Generated by Django 5.1.1 on 2024-10-08 13:39

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, help_text='Загрузите аватар', null=True, upload_to='users/image', verbose_name='Аватар'),
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='Укажите телефон', max_length=128, null=True, region='RU', verbose_name='Телефон'),
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('user', 'Пользователь'), ('admin', 'Администратор')], default='user', help_text='Укажите роль пользователя', max_length=10, verbose_name='Роль'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(db_index=True, help_text='Укажите E-mail', max_length=254, unique=True, verbose_name='E-mail'),
        ),
    ]