# littlelemonAPI/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import MenuItem, Booking

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ["id","title","price","inventory","featured","updated_at"]

class BookingSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Booking
        fields = ["id","user","name","guest_count","booking_date","special_requests","created_at"]

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ["id","username","email","password"]
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
