from django.urls import path

from . import views

urlpatterns = [
    path('', views.AuthorList.as_view(), name='author'),
    path('form/', views.author_form, name='author_insert'),
    path('form/<int:id>', views.author_form, name='author_update'),
]
