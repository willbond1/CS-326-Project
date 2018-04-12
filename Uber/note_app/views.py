from django.shortcuts import render, redirect
from django.views import generic
from .models import Note
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login

from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.db import transaction
from .models import Profile
from .forms import NoteForm, UserForm, ProfileForm

# Create your views here.
# def index(request):
#     num_users = User.objects.all().count()
#     num_notes = Note.objects.all().count()

#     return render(
#         request,
#         'index.html',
#         context={'num_users':num_users, 'num_notes':num_notes}
#     )

class DashboardView(generic.ListView):
    template_name = 'dashboard.html'
    context_object_name = 'recent_notes_list'
    queryset = Note.objects.all()

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['favorite_notes_list'] = Profile.objects.filter(user=self.request.user)[0].favorites.all()
        return context

class ProfileView(generic.ListView):
    template_name = 'profile.html'
    context_object_name = 'course_list'
    queryset = Note.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            #context['favorite_authors'] = Profile.objects.all()[0].fav_authors.all()
            context['favorite_course_notes'] = Profile.objects.filter(user=self.request.user)[0].favorites.all()
            #context['course_schedule'] = Profile.objects.all()[0].course_schedule.all()
        return context

class NoteDetailView(generic.DetailView):
    model = Note

class UpView(generic.ListView):
   template_name = 'uploaded_notes.html'
   context_object_name = 'recent_uploaded_notes_list'
   
   def get_queryset(self):
       return Profile.objects.filter(user=self.request.user)[0].uploaded.all()

class NoteCreateView(generic.edit.CreateView):
    def upload_notes(request):
        if request.method == "POST":
            form = NoteForm(request.POST, request.FILES)
            if form.is_valid():
                cur_note = form.save(commit=False)
                cur_note.author = request.user.profile
                cur_note.save()
                messages.success(request, ("Noteset successfully uploaded!"))
                return redirect('note-view',pk=cur_note.note_id)
        else:
            form = NoteForm()
    
        return render(request, "note_app/upload.html", {
            "form": form
        })

class ProfileCreateView(generic.edit.CreateView):
    def create_profile(request):
        if request.method == 'POST':
            user_form = UserForm(request.POST)
            profile_form = ProfileForm(request.POST, request.FILES)
            if user_form.is_valid() and profile_form.is_valid():
                user = user_form.save()
                profile = profile_form.save(commit=False)
                profile.user = user
                profile.profile_pic = profile_form.cleaned_data['profile_pic']
                profile.save()

                messages.success(request, ('Your profile was successfully created!'))
                return redirect('#LOGIN PAGE')
            else:
                messages.error(request, ('Please correct the error below.'))
        else:
            user_form = UserForm()
            profile_form = ProfileForm()
        return render(request, 'note_app/signup.html', {
            'user_form': user_form,
            'profile_form': profile_form
        })


class CommentCreateView(generic.edit.CreateView):
    def add_comment(request):
        if request.method == "POST":
            form = CommentForm(request.POST)
            if form.is_valid():
                cur_comm = form.save(commit=False)
                cur_comm.author = request.user.profile
                cur_comm.author.post_history.add(cur_comm)
                #ASSOCIATE COMMENT AND NOTESET WITH EACH OTHER
                form.save()
                return redirect('')
            else:
                form = CommentForm()

        return render(request, "", {"form": form})

class SearchView(generic.ListView):
    template_name = 'search.html'
    context_object_name = 'note_results'
    queryset = Note.objects.all()
