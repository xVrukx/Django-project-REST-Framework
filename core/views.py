#imports
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny ,IsAuthenticated
from rest_framework.response import Response
from core.tasks import send_email_task
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

#--------------------------------------------------------------
#registration via api
@api_view(['POST'])
@permission_classes([AllowAny])
def registeruser(request):
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')

    if not (username and password and email):
        return Response({'error': 'All fields are required'}, status=400)

    user = User.objects.create_user(username=username, password=password, email=email)
    user.save()

    # Send email asynchronously
    send_email_task.delay(
        subject='Welcome!',
        message=f'Hi {username}, thanks for registering!',
        recipient_list=[email])

    return Response({'message': 'User created successfully and welcome email sent!'})

#-----------------------------------------------------------
#Public view
@api_view(['GET'])
@permission_classes([AllowAny])
def public_view(request):
    return render(request, 'public.html')

#-----------------------------------------------------------
#Private/protected view
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_view(request):
    name = request.user.username
    return render(request, 'private.html',context= {'username': name})

#-----------------------------------------------------------
#home page
def home(request):
    return render(request, 'home.html')

#-----------------------------------------------------------
#registration page
def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if username and email and password:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            return redirect('login')
    return render(request, 'register.html')

#-----------------------------------------------------------
#login page
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')

#-----------------------------------------------------------
#logout function
def logout_view(request):
    logout(request)
    return redirect('login')