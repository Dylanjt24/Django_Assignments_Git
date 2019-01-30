from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User

# Create your views here.
def index(req):
    context = {
        'all_users': User.objects.all()
    }
    return render(req, 'users/index.html', context)

def create(req):
    errors = User.objects.validate(req.POST)
    if errors:
        for error in errors:
            messages.error(req, error)
        return redirect('users:new')
    User.objects.create_user(req.POST)
    return redirect('/users')

def new(req):
    return render(req, 'users/new.html')

def show(req, user_id):
    try:
        context = {
            'user': User.objects.get(id=user_id)
        }
    except:
        return redirect('users:index')
    return render(req, 'users/show.html', context)

def edit(req, user_id):
    try:
        context = {
            'user': User.objects.get(id=user_id)
        }
    except:
        return redirect('users:index')
    return render(req, 'users/edit.html', context)

def update(req, user_id):
    errors = User.objects.validate(req.POST)
    if errors:
        for error in errors:
            messages.error(req, error)
        return redirect('users:edit', user_id=user_id)
    User.objects.update_user(req.POST, user_id)
    return redirect('users:index')

def delete(req, user_id):
    try:
        User.objects.get(id=user_id).delete()
    except:
        return redirect('users:index')
    return redirect('users:index')