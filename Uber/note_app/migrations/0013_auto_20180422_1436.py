# Generated by Django 2.0.2 on 2018-04-22 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('note_app', '0012_remove_profile_favorites'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='author',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='posted_on',
        ),
        migrations.RemoveField(
            model_name='note',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='post_history',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
