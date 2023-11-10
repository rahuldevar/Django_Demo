"""
URL configuration for newproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [

    path('', views.Loginpage, name='Loginpage'),
    path('Signup', views.Signup, name='Signup'),


    path('home/', views.home, name='home'),
    path('logout/', views.logoutpage, name='logout'),
    path('success/', views.success, name='success'),

    path('detailsadd/', views.detailsadd, name='detailsadd'),

    path('booksearch/', views.booksearch, name='booksearch'),
    path('book_info/', views.book_info, name='book_info'),
    path('book_list/', views.book_list, name='book_list'),

    path('search/', views.search, name='search'),















]
