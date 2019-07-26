from django.contrib.auth.models import User
from rest_framework import serializers

# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'groups']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__' 