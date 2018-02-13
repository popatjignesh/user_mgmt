from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

def register(request):
	if request.method == 'POST':
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		email = request.POST['email']
		username = request.POST['username']
		email = request.POST['email']
		psw = request.POST['psw']
		repeat_psw = request.POST['repeat_psw']

		if psw == repeat_psw:
			user = User.objects.create_user(username, email , psw)
			user.save()
			return redirect('login')

	return render(request, 'account/registration.html', {})

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
			return render(request, 'account/login.html', {})

	return render(request, 'account/login.html', {})

def home(request):
	if request.method == 'POST':
		return redirect('logout')
	return render(request, 'home.html', {})

def userlogout(request):
	logout(request)
	return redirect('login')
