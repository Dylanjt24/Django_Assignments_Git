from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
import bcrypt

# Create your views here.
def index(req):
    return render(req, 'login/index.html')

def register(req):
    errors = User.objects.validate_registration(req.POST)
    if errors:
        for error in errors:
            messages.error(req, error)
        return redirect('login:index')
    messages.success(req, 'You have been successfully registered!')
    user = User.objects.create_user(req.POST)
    req.session['name'] = user.first_name
    req.session['user_id'] = user.id
    return redirect('login:success')

def login(req):
    errors = User.objects.validate_login(req.POST)
    if errors:
        for error in errors:
            messages.error(req, error)
        return redirect('login:index')
    messages.success(req, 'You have been successfully logged in!')
    user = User.objects.get(email=req.POST['email'])
    req.session['name'] = user.first_name
    req.session['user_id'] = user.id
    return redirect('login:success')

def success(req):
    if 'user_id' not in req.session:
        return redirect('login:index')
    return render(req, 'login/success.html')