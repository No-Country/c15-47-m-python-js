from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()


class Customer(models.Model):
    first_name = models.CharField(max_length=25, null=False)
    last_name = models.CharField(max_length=25, null=False)
    address = models.CharField(max_length=50, null=False)
    phone = models.CharField(max_length=25)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Category (models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Author (models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Publisher (models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Book (models.Model):
    isbn = models.IntegerField(null=False)
    title = models.CharField(max_length=100)
    id_publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    id_author = models.ForeignKey(Author, on_delete=models.CASCADE)
    year = models.IntegerField()
    id_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField(max_length=1000)
    stock = models.PositiveIntegerField(null=False)
    image = models.ImageField(upload_to="media/images")

    def __str__(self):
        return self.title


class Order(models.Model):
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)


class OrderBook (models.Model):
    id_customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    id_book = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(blank=False)

    def __str__(self):
        return f'Order: {self.id_order_book}'

    def total_order(self):
        return self.quantity * self.id_book.price
