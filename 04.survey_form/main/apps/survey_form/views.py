from django.shortcuts import render, HttpResponse, redirect
# Create your views here.
def index(req):
    return render(req, "survey_form/index.html")

def process(req):
    req.session['name'] = req.POST['name']
    req.session['location'] = req.POST['location']
    req.session['fav_language'] = req.POST['fav_language']
    req.session['comment'] = req.POST['comment']
    return redirect('/result')

def result(req):
    print('*' * 80)
    print(req.session['name'])
    return render(req, "survey_form/result.html")