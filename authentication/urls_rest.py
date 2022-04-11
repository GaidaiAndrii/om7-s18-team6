# from django.urls import path, include
# from . import views
# from rest_framework import routers
#
# router = routers.DefaultRouter()
# router.register('user', views.CustomUserView)
#
# # app_name = "authentication"
# # app_name = "user"
#
# urlpatterns = [
#     path('user/<int:user_pk>/order/<int:order_pk>/', views.ApiUserOrderPK.as_view()),
#     path('', include(router.urls)),
#     # path('<int:user_id>/order/<int:id>', views.UserOrderDetailGenerics.as_view(), name='user-order-detail'),
# ]
#
#
# # from . import views_rest
# #
# #
# # app_name = "authentication"
# #
# # urlpatterns = [
# #     path('', views_rest.CustomUserGenerics.as_view(), name='user-list'),
# #     path('<int:pk>/', views_rest.CustomUserDetailGenerics.as_view(), name='user-detail'),
# #     path('<int:user_id>/order/<int:id>', views_rest.UserOrderDetailGenerics.as_view(), name='user-order-detail')
# # ]