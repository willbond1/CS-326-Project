from django.urls import path
from . import views

urlpatterns = [
    path('',views.DashboardView.as_view(), name='dashboard'),
    path('note/<int:pk>', views.NoteDetailView.as_view(), name='note-detail')
]
