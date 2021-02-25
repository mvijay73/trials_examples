from django.urls import path
from setup import views

urlpatterns = [
    path("", views.home, name="home")
]
