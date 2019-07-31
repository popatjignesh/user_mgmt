# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

from rest_framework import status
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from rest_framework_jwt.settings import api_settings

from .serializers import UserSerializer, TokenSerializer

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        psw = request.POST['psw']
        repeat_psw = request.POST['repeat_psw']

        if psw == repeat_psw:
            user_obj = User.objects.create_user(username, email , psw)
            user_obj.first_name = first_name
            user_obj.last_name = last_name
            user_obj.save()
            return redirect('login')

    return render(request, 'account/registration.html', {})

def home(request):
    if request.method == 'POST':
        if request.user:
            return redirect('logout')
        else:
            return render(request, 'account/login.html', {})
    else:
        if request.user.id:
            return render(request, 'account/home.html', {})
        else:
            return redirect('login')

def userlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        psw = request.POST['psw']
        my_user = authenticate(username=username, password=psw)

        if my_user is not None:
            if my_user.is_active:
                login(request, my_user)
                return redirect('home')
        else:
            return render(request, 'account/login.html', {"error" : "Username or Password is incorrect...!"})

    return render(request, 'account/login.html', {})

def userlogout(request):
    logout(request)
    return redirect('login')



def JWTRegister(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        psw = request.POST['psw']
        repeat_psw = request.POST['repeat_psw']

        if psw == repeat_psw:
            user_obj = User.objects.create_user(username, email , psw)
            user_obj.first_name = first_name
            user_obj.last_name = last_name
            user_obj.save()
            return redirect('jwt_login')

    return render(request, 'account/jwt_registration.html', {})

def JWTHome(request):
    if request.method == 'POST':
        if request.user:
            return redirect('jwt_logout')
        else:
            return render(request, 'account/jwt_login.html', {})
    else:
        if request.user.id:
            return render(request, 'account/jwt_home.html', {})
        else:
            return redirect('jwt_login')

def JWTLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        psw = request.POST['psw']
        my_user = authenticate(request, username=username, password=psw)

        if my_user is not None:
            if my_user.is_active:
                login(request, my_user)

                serializer = TokenSerializer(data={
                    "token": jwt_encode_handler(
                        jwt_payload_handler(my_user)
                    )})
                if serializer.is_valid():
                    # return Response(serializer.data)
                    return redirect('jwt_home')
                else:
                    return render(request, 'account/jwt_login.html', serializer.errors)
            else:
                return render(request, 'account/jwt_login.html', {"error" : "This User is no longer active...!"})
        else:
            return render(request, 'account/jwt_login.html', {"error" : "Username or Password is incorrect...!"})

    return render(request, 'account/jwt_login.html', {})

def JWTLogout(request):
    logout(request)
    return redirect('jwt_login')

class UserDetails(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        queryset = User.objects.filter(id=self.request.user.id)
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
