from django.contrib import admin
from .models import User, Note

# Register your models here.
class NoteInline(admin.TabularInline):
    model = Note
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