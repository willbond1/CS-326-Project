from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key = True)
    user_name = models.CharField(max_length = 20, verbose_name = 'Username')
    first_name = models.CharField(max_length = 20, verbose_name = 'First Name')
    last_name = models.CharField(max_length = 20, verbose_name = 'Last Name')
    email = models.EmailField()
    favorites = models.ManyToManyField('note_app.Note')

    class Meta:
        ordering = ['user_name']
    
    def __str__(self):
        return '{0}, {1}'.format(self.last_name, self.first_name)
    
    # def get_absolute_url(self):
    #     return reverse('urlHERE', args=[str(self.user_id)])

class Note(models.Model):
    note_id = models.AutoField(primary_key = True)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    school = models.CharField(max_length = 50, verbose_name = 'School')
    title = models.CharField(max_length = 180, verbose_name = 'Title') # Can be changed to a date or whatever
    course = models.CharField(max_length = 40, verbose_name = 'Course')
    semester = models.CharField(max_length = 40, verbose_name = 'Semester')
    note_file = models.URLField(verbose_name='Note URL')
    
    class Meta:
        ordering = ['note_id']

    def __str__(self):
        return '{0}, {1}'.format(self.title, self.author)




