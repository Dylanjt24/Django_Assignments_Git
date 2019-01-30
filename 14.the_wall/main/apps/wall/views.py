from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.
def index(req):
    return render(req, 'wall/index.html')

def register(req):
    errors = User.objects.validate_registration(req.POST)
    if errors:
        for error in errors:
            messages.error(req, error)
        return redirect('main:index')
    user = User.objects.create_user(req.POST)
    req.session['user_id'] = user.id
    return redirect('main:wall')

def login(req):
    errors = User.objects.validate_login(req.POST)
    if errors:
        for error in errors:
            messages.error(req, error)
        return redirect('main:index')
    user = User.objects.get(email=req.POST['email'])
    req.session['user_id'] = user.id
    return redirect('main:wall')

def wall(req):
    if 'user_id' not in req.session:
        return redirect('main:index')
    context = {
        'user': User.objects.get(id=req.session['user_id']),
        'messages': Message.objects.all().order_by('-created_at'),
        'comments': Comment.objects.all()
    }
    return render(req, 'wall/wall.html', context)

def post_message(req):
    Message.objects.create_message(req.POST, req.session['user_id'])
    return redirect('main:wall')

def post_comment(req):
    Comment.objects.create_comment(req.POST, req.session['user_id'])
    return redirect('main:wall')

def delete_message(req, message_id):
    try:
        message = Message.objects.get(id=message_id)
    except:
        return redirect('main:wall')
    if message.message_creator.id != req.session['user_id']:
        messages.error(req, "Hey, that's not your message!")
        return redirect('main:logout')
    message.delete()
    return redirect('main:wall')

def logout(req):
    req.session.clear()
    return redirect('main:index')