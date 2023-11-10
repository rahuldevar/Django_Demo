from django.core.mail import message
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views import View
from numpy.core import records

from .models import login, signup, Book


# Create your views here.
@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')

def basehome(request):
    return render(request, 'basehome.html')
def success(request):
    return render(request, 'success.html')

def search(request):
    return render(request, 'search.html')

def Signup(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        var = signup(username=uname, email=email, password1=pass1, password2=pass2)
        var.save()

        if pass1 != pass2:
            return HttpResponse("Your password and confirm password are not Same!!")
        else:

            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect('Loginpage')

    return render(request, 'signup.html')


def Loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        var1 = login(username=username, password=pass1)
        var1.save()
        if user is not None:
            login(request, user)
            return redirect('search')
        else:
            return HttpResponse("Username or Password is incorrect!!!")
    return render(request, 'login.html')


def logoutpage(request):
    logout(request)
    return redirect('login')


class Referenceform:
    pass


def detailsadd(request):
    if request.method == 'GET':
        form = Referenceform()
    elif request.method == 'POST':
        form = Referenceform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request, 'detailsadd.html', {'form': form})

def booksearch(request):
    if request.method == 'GET':
        return render(request, 'booksearch.html')

    if request.method == 'POST':
        book_title = request.POST.get('booktitle')
        book_no = request.POST.get('booknumber')

        records = None
        message = None

        if book_title and book_no:
            records = Book.objects.filter(bookname=book_title)
        elif book_title:
            records = Book.objects.filter(bookname=book_title)
        elif book_no:
            records = Book.objects.filter(bookno=book_no)

        if records:
            return render(request, 'booksearch.html', {'search_book': records, 'message': message})
        elif book_title or book_no:
            message = "Book is not available"
        else:
            message = "Enter the details"

        return render(request, 'booksearch.html', {'search_book': records, 'message': message})


class BookForm:
    pass


def book_info(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = BookForm()

    return render(request, 'book_info.html', {'form': form})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})