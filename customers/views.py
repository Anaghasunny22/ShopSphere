# Import necessary Django shortcuts and modules
from django.shortcuts import render, redirect  # render: to show templates, redirect: to go to another URL
from django.contrib.auth.models import User     # User model for authentication
from django.contrib.auth import authenticate, login, logout  # functions to handle login/logout
from django.contrib import messages  # to show success or error messages in templates
from django.db import IntegrityError  # to handle duplicate entries (like same username)
from .models import Customer  # Import custom Customer model from this app

# View function to log out a user
def sign_out(request):
    logout(request)  # Log the user out (remove session)
    return redirect('home')  # Redirect to homepage after logout

# View function to handle account page (register and login)
def show_account(request):
    
    # ===========================
    # Handle user registration
    # ===========================
    if request.method == "POST" and 'register' in request.POST:  # Check if the form submitted is for registration
        try:
            # Get data from form fields
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            phone = request.POST.get('phone')

            # Create a new user with hashed password (built-in Django User model)
            user = User.objects.create_user(
                username=username,
                password=password,
                email=email
            )

            # Create a Customer object linked to this user
            Customer.objects.create(
                name=username,
                user=user,
                phone=phone
            )

            # Show success message to the user
            messages.success(request, "Account created successfully")
        
        except IntegrityError:
            # Handle duplicate username or invalid input
            error_message = "Duplicate Username or invalid input"
            messages.error(request, error_message)

    # ===========================
    # Handle user login
    # ===========================
    if request.method == "POST" and 'login' in request.POST:  # Check if the form submitted is for login
        username = request.POST.get('username')  # Get username from form
        password = request.POST.get('password')  # Get password from form
        
        # Check if user exists and password is correct
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)  # Log the user in (create session)
            return redirect('home')  # Redirect to homepage after login
        else:
            # Show error message if authentication fails
            messages.error(request, 'Invalid user credentials')

    # ===========================
    # Render the account page
    # ===========================
    return render(request, 'account.html')  # Show the account.html template
