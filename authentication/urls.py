from django.urls import path
from .views import *

urlpatterns = [
    path('', user_form, name='user_form'),
    path('<int:id>/', user_form, name='edit_user'),
    path('', UserList.as_view(), name='user'),
    path('overdue/', overdue, name='overdue')
]
