from django.contrib import admin
from .models import User, School, Professor, Course, Note

# Register your models here.
class UserInline(admin.TabularInline):
    model = User
    extra = 1

class NoteInline(admin.TabularInline):
    model = Note
    extra = 1

class SchoolInline(admin.TabularInline):
    model = School
    extra = 1

class CourseInline(admin.TabularInline):
    model = Course
    extra = 1

class ProfessorInline(admin.TabularInline):
    model = Professor
    extra = 1

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_name','user_id','last_name','first_name')
    inlines = [NoteInline]
    pass

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title','note_id','author','school','semester','course')
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