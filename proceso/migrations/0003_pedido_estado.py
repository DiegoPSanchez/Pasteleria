# Generated by Django 4.1.5 on 2023-02-16 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proceso', '0002_pedido_registro'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='estado',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
