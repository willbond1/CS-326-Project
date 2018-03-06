from django.shortcuts import render
from django.views import generic
from .models import User, Note

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
        context['favorite_notes_list'] = User.objects.all()[0].favorites.all()
        return context

class NoteDetailView(generic.DetailView):
    model = Note