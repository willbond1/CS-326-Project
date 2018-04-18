from django.contrib import admin
from .models import Profile, School, Professor, Course, Note

# Register your models here.
class ProfileInline(admin.TabularInline):
    model = Profile
    extra = 1

class NoteInline(admin.TabularInline):
    model = Note
    

class SchoolInline(admin.TabularInline):
    model = School
    extra = 1

class CourseInline(admin.TabularInline):
    model = Course
    extra = 1

class ProfessorInline(admin.TabularInline):
    model = Professor
    extra = 1

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user_username','user_last_name','user_first_name')
     

    def user_username(self,x):
        return x.user.username
    def user_last_name(self,x):
        return x.user.last_name
    def user_first_name(self,x):
        return x.user.first_name
    pass

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title','note_id','school','semester','course')
    pass

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('professor_id','first_name','last_name')
    inlines = [CourseInline]
    pass

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('school_id','name')
    inlines = [CourseInline, NoteInline]
    pass

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_id','title')
    inlines = [NoteInline]
    pass