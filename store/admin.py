from django.contrib import admin
from .models import Author, Book, Category, Customer, Publisher 

# Register your models here. To verify that all the models are registered
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Publisher)