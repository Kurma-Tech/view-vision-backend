from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.hashers import check_password
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .validators import validate_password

User = get_user_model()
from .models import Business


class UserSerializer(serializers.ModelSerializer):
    display_name = serializers.SerializerMethodField()

    @staticmethod
    def get_display_name(obj):
        return f"{obj.first_name} {obj.last_name}"
    
    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "status",
            "avatar",
            "gender",
            "display_name",
            "birth_date",
            "phone",
            "address",
            "whatsapp",
            "is_superuser",
            "is_admin",
            "is_staff",
        )

class AuthSerializer(serializers.Serializer):
    access_token = serializers.CharField(
        max_length=4096, required=True, trim_whitespace=True
    )

class RegistrationSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length = 64)
    last_name = serializers.CharField(max_length=64)
    email = serializers.EmailField(
        validators = [UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        write_only=True, validators=[validate_password]
    )

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
            "password",
        )

    def create(self, validated_data: dict) -> dict:
        user = User.objects.create_user(
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            email=validated_data["email"],
            password=validated_data["password"],
            status=User.UserStatusChoice.PENDING,
        )
        return user


class BusinessSerializer(serializers.Serializer):
    business_name = serializers.CharField(max_length=70)
    phone = serializers.CharField(max_length=20)
    email = serializers.EmailField(
        validators = [UniqueValidator(queryset=Business.objects.all())]
    )
    address = serializers.CharField(max_length=100)
    password = serializers.CharField(
        write_only=True, validators=[validate_password]
        
    )
    password2 = serializers.CharField(
        write_only=True, validators=[validate_password])
    class Meta:
        model = Business
        fields = ["business_name","phone", "email","password","password2"]
        
    def validate(self, attrs):
        business_queryset = Business.objects.all()
        print(business_queryset)
        
        # if business_queryset.exists() and business_queryset.count() ==1:
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"error":True, "info": "password & password2 didn't matched"})
        
        return attrs
    
            
    
    def create(self, validated_data):
        
        business = Business.objects.create(
            business_name = validated_data["business_name"],
            phone = validated_data["phone"],
            email = validated_data["email"],
            address = validated_data["address"],
            password = validated_data["password"]
            
        )
        return business 
        
        
    