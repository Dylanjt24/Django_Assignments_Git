from django.shortcuts import render, redirect, HttpResponse
import random
from time import strftime, localtime

# Create your views here.
def index(req):
    if 'gold' not in req.session:
        req.session['gold'] = 0
    if 'activities' not in req.session:
        req.session['activities'] = []
    return render(req, 'ninja_gold/index.html')

def process(req, location):
    if location == 'farm':
        earned = random.randint(10, 20)
        activity = "Earned " + str(earned) + " gold from the farm!"
        color = "green"
    elif location == 'cave':
        earned = random.randint(5, 10)
        activity = "Earned " + str(earned) + " gold from the cave!"
        color = "green"
    elif location == 'house':
        earned = random.randint(2, 5)
        activity = "Earned " + str(earned) + " gold from the house!"
        color = "green"
    elif location == 'casino':
        earned = random.randint(-50, 50)
        if earned >= 0:
            activity = "Earned " + str(earned) + " gold from the casino!"
            color = "green"
        else:
            activity = "Entered a casino and lost " + str(abs(earned)) + " gold... Ouch.."
            color = "red"
    else:
        return redirect('/')
    req.session['gold'] += earned
    time = strftime('%d/%m/%Y %I:%M%p', localtime())
    temp_list = req.session['activities']
    temp_list.append({"activity": activity, "time": time, "color": color })
    req.session['activities'] = temp_list
    return redirect('/')

def clear(req):
    req.session.clear()
    return redirect('/')