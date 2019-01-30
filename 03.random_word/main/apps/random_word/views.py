from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(req):
    if 'count' not in req.session:
        req.session['count'] = 0
    else:
        req.session['count'] += 1
    context = {
        'word': get_random_string(length=14)
    }
    return render(req, 'random_word/index.html', context)

def reset(req):
    req.session['count'] = 0
    return redirect('/random_word')