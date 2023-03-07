from django.urls import path
from . import views

urlpatterns = [
    path("", views.oceania, name="oceania"),
    path("novazelandia", views.novazelandia, name="novazelandia"),
    path("australia", views.australia, name="australia"),
]