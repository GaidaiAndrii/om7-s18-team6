from django.urls import path

from . import views

urlpatterns = [
    path('form/', views.add_order, name='add_order'),
    path('form/<int:id>/', views.add_order, name='add_order'),
    path('', views.OrderList.as_view(), name='order'),
    path('<int:order_id>', views.order_by_id, name='order_by_id'),
]
