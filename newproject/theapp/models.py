from django.db import models


# Create your models here.
class login(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


class signup(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password1 = models.CharField(max_length=100)
    password2 = models.CharField(max_length=100)

class detailsadd(models.Model):
    breweryName = models.CharField(max_length=100)
    breweryAddress = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=100)
    websiteURL = models.CharField(max_length=100)
    currentRating = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)


class Book(models.Model):
    bookname = models.CharField(max_length=100)
    authorname = models.CharField(max_length=100)
    bookno = models.CharField(max_length=10)
    edition = models.CharField(max_length=20,null=True)
    status= models.CharField(max_length=20,null=True)


class Add(models.Model):
    bookname = models.CharField(max_length=100)
    authorname = models.CharField(max_length=100)
    bookno = models.CharField(max_length=10)
    edition = models.CharField(max_length=20,null=True)
    status= models.CharField(max_length=20,null=True)