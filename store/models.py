from django.db import models
from django.db import User


# Create your models here.
class Cunstomer(models.Model):
    name= models.CharField(max_length=25)
    adrress= models.CharField(max_length=50)
    phone= models.IntegerField()
    id_user= models.ForeignKey(User)


class Order_Book(models.Model):
    book_isbn= models.models.IntegerField()

class Order (models.Model):
    id_customer= models.ForeignKey(Cunstomer)
    id_order_book=models.ForeignKey(Order_Book)






class Category (models.Model):
    name= models.CharField(max_length=50)

class Author (models.Model):
    name= models.CharField(max_length=100)
    country= models.CharField(max_length=100)
    
class Publisher (models.Model):
    name= models.CharField(max_length=100)
    country= models.CharField(max_length=100)


class Book (models.Model):
    isbn= models.IntegerField()
    title= models.CharField(max_length=100)
    id_publisher= models.ForeignKey(Publisher)
    id_author= models.ForeignKey(Author)
    year= models.IntegerField()
    id_category= models.ForeignKey(Category)
    price= models.DecimalField()    
    description= models.TextField(max_length=1000)
    stock= models.IntegerField()
    image = models.ImageField(upload_to="media/images")