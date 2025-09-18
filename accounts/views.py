from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from .models import Profile
import re

def signup(request):
    relation_choices = Profile.RELATION_CHOICES  # for dropdown

    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        relation = request.POST.get("relation")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        # Check passwords match
        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return render(request, "accounts/signup.html", {"relation_choices": relation_choices})

        # Check username exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return render(request, "accounts/signup.html", {"relation_choices": relation_choices})

        # Validate Saudi phone number (966XXXXXXXXX)
        if not re.fullmatch(r'966\d{9}', phone):
            messages.error(request, "Phone number must start with 966 and have 9 more digits")
            return render(request, "accounts/signup.html", {"relation_choices": relation_choices})

        # Create user and profile
        user = User.objects.create_user(username=username, email=email, password=password1)
        Profile.objects.create(user=user, phone=phone, relation=relation)
        auth_login(request, user)
        return redirect("home")

    return render(request, "accounts/signup.html", {"relation_choices": relation_choices})

def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            auth_login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials")
    return render(request, "accounts/login.html")