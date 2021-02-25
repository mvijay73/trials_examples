from django.urls import path
from setpyenv import views

urlpatterns = [
    path("", views.home, name="home"),
]