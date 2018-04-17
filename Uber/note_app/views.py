from django.shortcuts import render, redirect
from django.views import generic
from .models import Note
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.db import transaction
from .models import Profile
from .forms import NoteForm, UserForm, ProfileForm
from .forms import CustomUserCreationForm
from django.views.generic.edit import CreateView, UpdateView
 

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

     

class ProfileView(generic.ListView):
    template_name = 'profile.html'
    context_object_name = 'course_list'
    queryset = Note.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        

class NoteDetailView(generic.DetailView):
    model = Note

class UpView(generic.ListView):
   template_name = 'uploaded_notes.html'
   context_object_name = 'recent_uploaded_notes_list'
   queryset = Note.objects.all()


class NoteCreateView(generic.edit.CreateView):
    def upload_notes(request):
        if request.method == "POST":
            form = NoteForm(request.POST, request.FILES)
            if form.is_valid():
                 
                cur_note = form.save(commit=False)
                cur_note.save()
                messages.success(request, ("Noteset successfully uploaded!"))
                return redirect('note-view',pk=cur_note.note_id)
        else:
            form = NoteForm()
    
        return render(request, "note_app/upload.html", {
            "form": form
        })

def register(request):
    if request.method == 'POST':
        f = CustomUserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return redirect('/')

    else:
        f = CustomUserCreationForm()

    return render(request, 'note_app/register.html',{
            "form": f
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

class SearchResultsView(generic.ListView):
    template_name = 'search.html'
    context_object_name = 'note_results'

    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            return Note.objects.filter(title__contains=query)
        else:
            return []
    
@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            return redirect('settings:profile')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'note_app/profile_up.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

class NoteUpdate(UpdateView):
   model = Note
   fields = ["note_file", "thumbnail", "title", "school", "course", "semester"]    
   success_url = '/'