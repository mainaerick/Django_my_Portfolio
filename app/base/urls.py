from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('downloadpdf/<str:filename>/',
         views.download_pdf_file, name='download_pdf_file'),
]
