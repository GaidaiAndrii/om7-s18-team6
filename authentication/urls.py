from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('user', views.CustomUserView)

urlpatterns = [
    path('form', views.user_form, name='user_form'),
    path('<int:id>/', views.user_form, name='edit_user'),
    path('all/', views.UserList.as_view(), name='users'),
    path('overdue/', views.overdue, name='overdue'),
    path('', include(router.urls))
]
