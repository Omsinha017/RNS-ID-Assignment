# notes_project/urls.py
from django.contrib import admin
from django.urls import path
from notes.views import NoteListAPIView, NoteDetailAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/notes/', NoteListAPIView.as_view(), name='note-list'),
    path('api/notes/<int:pk>/', NoteDetailAPIView.as_view(), name='note-detail'),
]
