# Generated by Django 3.1.1 on 2023-07-17 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SelectionApp', '0008_auto_20230717_1816'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='availability',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
