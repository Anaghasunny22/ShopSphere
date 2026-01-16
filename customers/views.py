from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.db import IntegrityError
from .models import Customer

def sign_out(request):
    logout(request)
    return redirect('home')

def show_account(request):
    if request.method == "POST" and 'register' in request.POST:
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            phone = request.POST.get('phone')

            # Create user (hashed password)
            user = User.objects.create_user(
                username=username,
                password=password,
                email=email
            )

            # Create customer
            Customer.objects.create(
                name=username,
                user=user,
                phone=phone
            )
            messages.success(request, "Account created successfully")
            

        except IntegrityError:
            error_message="Duplicate Username or invalid input"  # or handle error properly
            messages.error(request,error_message)

    if request.method == "POST" and 'login' in request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'invalid user credientials')

    return render(request, 'account.html')
