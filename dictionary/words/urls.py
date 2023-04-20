from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("<str:phyrexian_word_str>/", views.word_entry, name="word_entry")
]