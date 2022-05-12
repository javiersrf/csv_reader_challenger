from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('home', views.index, name='index'),
    path('upload', views.upload_file, name='upload'),
    path('success', views.index, name='success')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)