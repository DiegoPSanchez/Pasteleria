# Generated by Django 4.1.5 on 2023-01-21 04:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='proyectos',
            old_name='title',
            new_name='titulo',
        ),
    ]
