from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key = True)
    user_name = models.CharField(max_length = 20, verbose_name = 'Username')
    first_name = models.CharField(max_length = 20, verbose_name = 'First Name')
    last_name = models.CharField(max_length = 20, verbose_name = 'Last Name')
    email = models.EmailField()
    favorites = models.ManyToManyField('note_app.Note', related_name="favorites", blank=True)
    uploaded = models.ManyToManyField('note_app.Note', related_name="uploaded", blank=True)


    class Meta:
        ordering = ['user_name']
    
    def __str__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)

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
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    school = models.ForeignKey(School, on_delete = models.CASCADE)
    title = models.CharField(max_length = 180, verbose_name = 'Title') # Can be changed to a date or whatever
    course = models.ForeignKey(Course, on_delete = models.CASCADE)
    semester = models.CharField(max_length = 40, verbose_name = 'Semester')
    note_file = models.URLField(verbose_name='Note URL')
    
    class Meta:
        ordering = ['note_id']

    def __str__(self):
        return '{0}, {1}'.format(self.title, self.author)
