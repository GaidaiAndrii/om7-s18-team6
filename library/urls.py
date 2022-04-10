"""djangoViewTemplates URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('404/', not_found_404, name='not_found_404'),
    path('api/v1/',   include("authentication.urls"), name="user"),
    path('api/v1/', include("author.urls"), name="author"),
    path('api/v1/',   include("book.urls")),
    path('api/v1/',  include("order.urls"), name="order"),
    path('statistics/', statistics, name="statistics"),
    path('rules/', rules, name="rules"),
    path('reconstruction/', reconstruction, name="reconstruction"), 
]

# handler404 = not_found_404