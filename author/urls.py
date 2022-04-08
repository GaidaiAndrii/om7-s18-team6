from django.urls import path
from .views import *

urlpatterns = [
    path('form/', author_form, name='author_insert'),
    path('form/<int:id>', author_form, name='author_update'),
    path('', AuthorList.as_view(), name='author'),
]
