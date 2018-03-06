from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView



urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('note_app/', include('note_app.urls')),
]

urlpatterns += [
    path('', RedirectView.as_view(url='/note_app/', permanent=True)),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


