from django.shortcuts import render
from django.views import generic
from .models import Note
from django.contrib.auth.models import User

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
        context['favorite_notes_list'] = Note.objects.all()
#Profile.objects.all()[0].favorites.all()
        return context

class ProfileView(generic.ListView):
    template_name = 'profile.html'
    context_object_name = 'course_list'
    queryset = Profile.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['favorite_authors'] = Note.objects.all()
#Profile.objects.all()[0].fav_authors.all()
        context['favorite_course_notes'] = Note.objects.all()
#Profile.objects.all()[0].favorites.all()
        context['course_schedule'] = Note.objects.all()
#Profile.objects.all()[0].course_schedule.all()
        return context

class NoteDetailView(generic.DetailView):
    model = Note

class UpView(generic.ListView):
   template_name = 'uploaded_notes.html'
   context_object_name = 'recent_uploaded_notes_list'
   queryset = Note.objects.all()
#Profile.objects.all()[0].uploaded.all()

class NoteCreateView(generic.edit.CreateView):
    def upload_notes(request):
        if request.method == "POST":
            form = NoteForm(request.POST, request.FILES)
            if form.is_valid():
                cur_note = form.save(commit=False)
                cur_note.author = request.user.profile
                cur_note.save()
                messages.success(request, _("Noteset successfully uploaded!"))
                return redirect("note-upload")
        else:
            form = NoteForm()
    
        return render(request, "note_app/upload.html", {
            "form": form
        })

class ProfileCreateView(generic.edit.CreateView):
    def create_profile(request):
        if request.method == 'POST':
            user_form = UserForm(request.POST, instance=request.user)
            profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                profile_form.save()
                messages.success(request, _('Your profile was successfully created!'))
                return redirect('')
            else:
                messages.error(request, _('Please correct the error below.'))
        else:
            user_form = UserForm(instance=request.user)
            profile_form = ProfileForm(instance=request.user.profile)
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
                return redirect("")
            else:
                form = CommentForm()

        return render(request, "", {"form": form})
