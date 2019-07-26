from rest_framework import status, viewsets
from django.contrib.auth.models import User
from account.serializers  import *

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer