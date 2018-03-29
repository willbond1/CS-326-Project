from django.shortcuts import render
from django.views import generic
from .models import Note
from django.contrib.auth.models import User

from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.db import transaction

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
        context['favorite_notes_list'] = Profile.objects.all()[0].favorites.all()
        return context

class NoteDetailView(generic.DetailView):
    model = Note

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