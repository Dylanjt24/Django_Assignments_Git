from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def index(req):
    context = {
        'all_courses': Course.objects.all()
    }
    return render(req, 'courses/index.html', context)

def create(req):
    errors = Course.objects.validate(req.POST)
    if errors:
        for error in errors:
            messages.error(req, error)
        return redirect('courses:index')
    Course.objects.create_course(req.POST)
    return redirect('courses:index')

def destroy(req, course_id):
    try:
        context = {
            'course': Course.objects.get(id=course_id)
        }
    except:
        return redirect('courses:index')
    return render(req, 'courses/destroy.html', context)

def delete(req, course_id):
    errors = []
    try:
        Course.objects.get(id=course_id).delete()
    except:
        errors.append('Course could not be deleted.')
        for error in errors:
            messages.error(req, error)
        return redirect('courses:delete', course_id)
    return redirect('courses:index')