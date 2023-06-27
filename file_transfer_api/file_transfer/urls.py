from django.urls import path

from .views import FileListView, UploadFileView

urlpatterns = [
    path("files/", FileListView.as_view()),
    path("upload/", UploadFileView.as_view()),
]
