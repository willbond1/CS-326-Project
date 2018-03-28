from django import forms
from django.contrib.auth.models import User
from .models import Profile, Note, Comment

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ["note_file", "thumbnail", "title", "school", "course", "semester"]

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', "password")

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("bio", "profile_pic")

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["body"]