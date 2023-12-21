from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Customer, Book, Category
import contextlib
import random

User = get_user_model()


class IndexView(View):    
    def get(self, request, **kwargs):
        context = {}
        try:
            user = User.objects.get(id=request.user.id)
            context["user"] = user
        except User.DoesNotExist:
            user = None
        try:
            customer = Customer.objects.get(id_user_id=user)
            context["customer"] = customer
        except Customer.DoesNotExist:
            pass
        context['categories'] = Category.objects.all()
        context['popular_books'] = Book.objects.all()
        return render(request, "index.html", context)

class BookListView(ListView):
    model: Book
    context_object_name = 'books'
    queryset = Book.objects.order_by('title')
    # ordering = ['title']
    template_name = 'book_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class BookDetail(View):
    template_name = "book_details.html"
    
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        context = {'book': book}
        context['popular_books'] = Book.objects.all()
        return render(request, self.template_name, context)

def success(request):
    template_name="success.html"
    return render(request, template_name)
