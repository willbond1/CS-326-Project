from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key = True)
    user_name = models.CharField(max_length = 20, verbose_name = 'Username')
    first_name = models.CharField(max_length = 20, verbose_name = 'First Name')
    last_name = models.CharField(max_length = 20, verbose_name = 'Last Name')
    email = models.EmailField()
    favorites = models.ManyToManyField('note_app.Note')
    uploaded = models.ManyToManyField('note_app.Note')


    class Meta:
        ordering = ['user_name']
    
    def __str__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)
    
    

class Note(models.Model):
    note_id = models.AutoField(primary_key = True)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    school = models.ForeignKey(School, on_delete = models.CASCADE)
    title = models.CharField(max_length = 180, verbose_name = 'Title') # Can be changed to a date or whatever
    course = models.CharField(max_length = 40, verbose_name = 'Course')
    semester = models.CharField(max_length = 40, verbose_name = 'Semester')
    note_file = models.URLField(verbose_name='Note URL')
    
    class Meta:
        ordering = ['note_id']

    def __str__(self):
        return '{0}, {1}'.format(self.title, self.author)

class School(models.Model):
    school_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 50, verbose_name = "Name")

class Course(models.Model):
    course_id = models.AutoField(primary_key = True)
    title = models.CharField(max_length = 30, verbose_name = 'Title')
    school = models.ForeignKey(School, on_delete = models.CASCADE)
