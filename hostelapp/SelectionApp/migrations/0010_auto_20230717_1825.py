# Generated by Django 3.1.1 on 2023-07-17 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SelectionApp', '0009_room_availability'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='students', to='SelectionApp.room'),
        ),
    ]