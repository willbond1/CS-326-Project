# Generated by Django 2.0.4 on 2018-04-18 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('note_app', '0010_remove_note_karma'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='note',
            options={},
        ),
        migrations.RemoveField(
            model_name='profile',
            name='uploaded',
        ),
    ]
