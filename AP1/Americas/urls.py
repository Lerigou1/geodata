from django.urls import path
from . import views

urlpatterns = [
    path("", views.americas, name="americas"),
    path("canada", views.canada, name="canada"),
    path("colombia", views.colombia, name="colombia"),
    path("mexico", views.mexico, name="mexico"),
]