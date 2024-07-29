from django.urls import path
from .views import TranscribeVideo
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='transcriptions/index.html')),
    path('api/transcribe/', TranscribeVideo.as_view()),
]
