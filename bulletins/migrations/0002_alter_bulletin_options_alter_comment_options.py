# Generated by Django 5.1.1 on 2024-10-10 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bulletins', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bulletin',
            options={'ordering': ['-created_at'], 'verbose_name': 'Объявление', 'verbose_name_plural': 'Объявления'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created_at'], 'verbose_name': 'Комментарий', 'verbose_name_plural': 'Комментарии'},
        ),
    ]
