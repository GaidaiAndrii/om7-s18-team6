from django.urls import path
from .views import *

urlpatterns = [
    path('', user_form, name='user_form'),
    path('<int:id>/', user_form, name='edit_user'),
    path('all/', UserList.as_view(), name='users'),
    path('overdue/', overdue, name='overdue')
]
