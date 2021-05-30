from rest_framework import  serializers
from .models import  Request
from django.contrib.auth import  get_user_model


User = get_user_model()

class CreateRequestSerializer(serializers.ModelSerializer):
    class  Meta:
        model=Request
        fields=['username', "request_type", "application", "windows_id", "current_branch","current_role", "line_manager", "zonal", "requester_comment"]


class ListRequestSerializer(serializers.ModelSerializer):
    class  Meta:
        model=Request
        fields="__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User,
        fields=['id','email','username']

