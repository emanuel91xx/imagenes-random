from django.urls import path
from . import views

app_name = "gallery"

urlpatterns = [
    path("", views.home, name="home"),
    path("api/random-photo/", views.random_photo_api, name="random_photo_api"),
]
