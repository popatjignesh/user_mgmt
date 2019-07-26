# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import UserSerializer

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
        return redirect('logout')
    return render(request, 'account/home.html', {})

def userlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        psw = request.POST['psw']
        my_user = authenticate(username=username, password=psw)
        print "my_user = ", my_user

        if my_user is not None:
            if my_user.is_active:
                login(request, my_user)
                return redirect('home')
        else:
            return render(request, 'account/login.html', {"error" : "Please enter Correct Password...!"})

    return render(request, 'account/login.html', {})

def userlogout(request):
    logout(request)
    return redirect('login')

class UserDetails(APIView):
    def get(self, request, format=None):
        queryset = User.objects.filter(id=self.request.user.id)
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)