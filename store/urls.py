from django.urls import path

from . import views
from .views import IndexView, BookListView, BookDetail

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("books", BookListView.as_view(), name="books"),
    path("book/<int:pk>/", BookDetail.as_view(), name="book"),
]