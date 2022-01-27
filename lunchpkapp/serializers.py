from rest_framework import serializers
import rest_framework
from drf_extra_fields.fields import Base64ImageField
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, get_user_model
from django.utils.translation import ugettext_lazy as _
from .models import *


UserModel = get_user_model()


class DealsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Deals
        fields = '__all__'

class frozenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Frozen
        fields = ['id', 'name', "frzn_img", "persons", "pieces", "price"]



class MonthlySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MonthlyPackage
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id', 'first_name', 'last_name', 'username', 'email', 'password', 'is_staff')


class SignupSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = UserModel.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )

        return user

    class Meta:
        model = UserModel
        fields = ('id', 'first_name', 'last_name', 'username', 'email', 'password')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')