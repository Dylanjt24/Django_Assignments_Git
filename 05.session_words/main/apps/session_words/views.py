from django.shortcuts import render, HttpResponse, redirect
from time import strftime, localtime

# Create your views here.
def index(req):
    return render(req, 'session_words/index.html')

def add_word(req):
    if 'words' not in req.session:
        req.session['words'] = []
    time_created = strftime('%I:%M:%S%p, %b %d %Y', localtime())
    temp_list = req.session['words']
    temp_list.append({"word": req.POST['word'], "color": req.POST['color'], "font_weight": req.POST['big_font'], "time": time_created})
    req.session['words'] = temp_list
    print(req.session['words'])
    return redirect('/session_words/')

def clear(req):
    req.session.clear()
    return redirect('/session_words/')