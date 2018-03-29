from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    profile_id = models.AutoField(primary_key = True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name = "profile")
    bio = models.TextField(max_length=500, blank=True)
    favorites = models.ManyToManyField('note_app.Note', related_name="favorites", blank=True)
    uploaded = models.ManyToManyField('note_app.Note', related_name="uploaded", blank=True)
    profile_pic = models.ImageField(upload_to="../static/note_app/assets/profiles/")
    post_history = models.ManyToManyField("note_app.Comment", related_name="post_history", blank=True)
    karma = models.SmallIntegerField(default=0)
    #favorite_authors = models.ManyToManyField('note_app.Profile', related_name = "fav_authors", blank=True)
    #course_schedule = models.ManyToManyField('note_app.Course', related_name = "course_schedule", blank=True)

    class Meta:
        ordering = ['profile_id']
    
    def __str__(self):
        return '{0} {1}'.format(self.user.first_name, self.user.last_name)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

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
    school = models.ForeignKey(School, on_delete = models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete = models.CASCADE)

    def __str__(self):
        return '{0}'.format(self.title)

class Note(models.Model):
    note_id = models.AutoField(primary_key = True)
    note_file = models.FileField(upload_to="../static/note_app/assets/notes/")
    thumbnail = models.ImageField(upload_to="../static/note_app/assets/thumbnails/", blank=True)
    author = models.ForeignKey(Profile, on_delete = models.CASCADE)
    school = models.ForeignKey(School, on_delete = models.CASCADE)
    title = models.CharField(max_length = 180, verbose_name = 'Title') # Can be changed to a date or whatever
    course = models.ForeignKey(Course, on_delete = models.CASCADE)
    semester = models.CharField(max_length = 40, verbose_name = 'Semester')
    # note_file = models.URLField(verbose_name='Note URL')
    date_uploaded = models.DateTimeField(auto_now_add=True)
    comments = models.ManyToManyField("note_app.Comment", related_name="comments", blank=True)
    karma = models.SmallIntegerField(default=0)
    
    class Meta:
        ordering = ['note_id']

    def __str__(self):
        return '{0}, {1}'.format(self.title, self.author)

class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    body = models.TextField(max_length=500)
    karma = models.SmallIntegerField(default=0)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    posted_on = models.ForeignKey(Note, on_delete=models.CASCADE)

    class Meta:
        ordering=["date_uploaded"]

    def __str__(self):
        return "Posted by {0} at {1} with a score of {2}: {3}".format(self.title, self.date_uploaded, self.karma, self.body)
