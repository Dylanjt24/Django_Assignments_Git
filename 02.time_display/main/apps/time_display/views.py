from django.shortcuts import render, HttpResponse, redirect
from time import localtime, strftime

# Create your views here.
def index(req):
    context = {
        "time": strftime("%b %d, %Y %I:%M %p", localtime())
    }
    return render(req, 'time_display/index.html', context)