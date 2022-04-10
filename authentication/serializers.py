from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("id", "url", "first_name", "middle_name", "last_name", 
                  "email", "password", "role", "orders")