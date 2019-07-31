from django.conf.urls import url
from account import views
# from rest_framework_simplejwt import views as jwt_views
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    # url(r'^account/register', views.register, name='register'),
    # url(r'^account/home', views.home, name='home'),
    # url(r'^account/login', views.userlogin, name='login'),
    # url(r'^account/logout', views.userlogout, name='logout'),

    # url(r'^api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # url(r'^api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    url(r'^api-token-auth/', obtain_jwt_token, name='create-token'),

    url(r'^api/jwt-register', views.JWTRegister, name='jwt_register'),
    url(r'^api/jwt-home', views.JWTHome, name='jwt_home'),
    url(r'^api/jwt-login', views.JWTLogin, name='jwt_login'),
    url(r'^api/jwt-logout', views.JWTLogout, name='jwt_logout'),

    url(r'^api/user-details', views.UserDetails.as_view(), name='use_details'),
]
