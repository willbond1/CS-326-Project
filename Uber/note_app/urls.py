from django.urls import path
from . import views

urlpatterns = [
    path('',views.DashboardView.as_view(), name='dashboard-view'),
    path('note/<int:pk>', views.NoteDetailView.as_view(), name='note-view'),
    path("upload/", views.NoteCreateView.upload_notes, name="note-upload"),
    path("signup/", views.ProfileCreateView.create_profile, name="profile-signup"),
]
