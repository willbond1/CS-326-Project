# Generated by Django 2.0.4 on 2018-04-15 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('note_app', '0004_auto_20180403_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='note_app.School'),
        ),
    ]
