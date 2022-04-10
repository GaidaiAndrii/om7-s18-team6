from django.urls import path

from . import views

urlpatterns = [
    path('form', views.user_form, name='user_form'),
    path('<int:id>/', views.user_form, name='edit_user'),
    path('all/', views.UserList.as_view(), name='users'),
    path('overdue/', views.overdue, name='overdue'),
]
