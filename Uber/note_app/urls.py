from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.DashboardView.as_view(), name='dashboard-view'),
    path('note/<int:pk>', views.NoteDetailView.as_view(), name='note-view')
]

