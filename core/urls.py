#imports
from django.urls import path
from .views import *
from rest_framework.authtoken.views import obtain_auth_token

#--------------------------------------------------------------
#Url paths
urlpatterns = [
    path('public/', public_view, name='public'),
    path('private/', protected_view, name='private'),

    # API endpoints
    path('api/login/', obtain_auth_token, name='api_login'),
    path('api/register/', registeruser, name='api_register'),

    # Web pages
    path('', home, name='home'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]