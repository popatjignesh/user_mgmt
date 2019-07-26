from django.conf.urls import url
from account import views

urlpatterns = [
    url(r'^account/home', views.home, name='home'),
    url(r'^account/register', views.register, name='register'),
    url(r'^account/login', views.userlogin, name='login'),
    url(r'^account/logout', views.userlogout, name='logout'),

    url(r'^account/user-details', views.UserDetails.as_view(), name='user-details'),
]
