from django.urls import path
from .views import IndexView, BookListView, BookDetail
from . import views

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("books", BookListView.as_view(), name="books"),
    path("book/<int:pk>/", BookDetail.as_view(), name="book"),
    path("category/<str:foo>", views.category, name="category"),
]