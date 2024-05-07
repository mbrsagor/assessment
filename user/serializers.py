from django.contrib.auth import password_validation
from rest_framework import serializers

from .models import User


class RegistrationSerializer(serializers.ModelSerializer):
    """
    Name: User registration for web serializer
    """

    password = serializers.CharField(style={'input_type': 'password', 'placeholder': 'Password'})

    class Meta:
        model = User
        fields = (
            'id', 'email', 'full_name', 'phone', 'role', 'password'
        )

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            full_name=validated_data['full_name'],
            phone=validated_data['phone'],
            role=validated_data['role'],
            password=validated_data['password'],
        )
        return user

    # Password validation here
    def validated_password(self, value):
        password_validation.validate_password(value, self.instance)
        return value

    """def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email already exists!.")
        return value"""


class UserSerializer(serializers.ModelSerializer):
    """
    Name: User list serializer
    """

    class Meta:
        model = User
        fields = [
            'id', "uuid", 'email', 'full_name', 'phone',
            'role', 'address', 'avatar', 'is_active',
            'is_staff', 'is_superuser', 'date_joined'
        ]


class UserProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'full_name', 'email', 'phone',
            'role', 'address', 'avatar'
        )


class PasswordChangeSerializer(serializers.Serializer):
    """
    Name: Password Change Serializer
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
