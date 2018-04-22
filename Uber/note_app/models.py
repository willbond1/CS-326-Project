from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    bio = models.TextField(max_length=500, blank=True)
    profile_pic = models.ImageField(upload_to="../media/profiles/")
    karma = models.SmallIntegerField(default=0)

class School(models.Model):
    school_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 50, verbose_name = "Name")

    def __str__(self):
        return '{0}'.format(self.name)

class Professor(models.Model):
    professor_id = models.AutoField(primary_key = True)
    first_name = models.CharField(max_length = 20, verbose_name = 'First Name')
    last_name = models.CharField(max_length = 20, verbose_name = 'Last Name')

    def __str__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)

class Course(models.Model):
    course_id = models.AutoField(primary_key = True)
    title = models.CharField(max_length = 30, verbose_name = 'Title')
    school = models.ForeignKey(School,null=True, on_delete = models.SET_NULL)
    professor = models.ForeignKey(Professor, null=True, on_delete = models.SET_NULL)

    def __str__(self):
        return '{0}'.format(self.title)

class Note(models.Model):
    note_id = models.AutoField(primary_key = True)
    author = models.ForeignKey(User, related_name="notes", on_delete=models.CASCADE, default=1)
    note_file = models.FileField(upload_to="../media/notes/")
    thumbnail = models.ImageField(upload_to="../media/thumbnails/", blank=True)
    school = models.ForeignKey(School, null=True, on_delete = models.SET_NULL)
    title = models.CharField(max_length = 180, verbose_name = 'Title')
    course = models.ForeignKey(Course, null=True, on_delete = models.SET_NULL)
    semester = models.CharField(max_length = 40, verbose_name = 'Semester')
    date_uploaded = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date_uploaded"]

    def __str__(self):
        return '{0}'.format(self.title) 