# Generated by Django 2.0.2 on 2018-03-06 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note_app', '0002_auto_20180305_2320'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='favorites',
            field=models.ManyToManyField(to='note_app.Note'),
        ),
    ]
