from django.urls import path
from . import views

urlpatterns = [
    path("article/<int:id>/", views.show_article, name="show_article"),
]