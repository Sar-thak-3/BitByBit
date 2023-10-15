from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload, name = 'file_upload'),
    path('final/', views.download, name = 'download_docx'),
    path('download/', views.download_page, name = 'down')
]
