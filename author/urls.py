from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('author', views.AuthorView)

urlpatterns = [
    path('', views.AuthorList.as_view(), name='author'),
    path('form/', views.author_form, name='author_insert'),
    path('form/<int:id>', views.author_form, name='author_update'),
    path('', include(router.urls)),
]
