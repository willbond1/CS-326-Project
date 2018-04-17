from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
 

urlpatterns = [
    path('',views.DashboardView.as_view(), name='dashboard-view'),
    path('note/<int:pk>', views.NoteDetailView.as_view(), name='note-view'),
    path('uploaded/', views.UpView.as_view(),name='upload-view'),
    path("upload/", views.NoteCreateView.upload_notes, name="note-upload"),
    path('signup/', views.register , name='profile-signup'),
    path('profile/', views.ProfileView.as_view(), name = 'profile-view'),
    path('search/', views.SearchView.as_view(), name='search-view'),
    path('search/results', views.SearchResultsView.as_view(), name='search-results-view'),
]

urlpatterns += [  
path('profile/<int:pk>/update/', views.update_profile , name='profile_up-view'),
]
