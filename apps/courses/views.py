from django.shortcuts import render, redirect
from . import models
import datetime


# Create your views here.
def index(request):
    courses = models.Course.objects.all()
    print courses
    context = { 'courses': courses}
    return render(request, "courses/index.html", context)

def submit(request):
    name = request.POST['name']
    description = request.POST['description']
    time = datetime.datetime.now()
    query = models.Course(name = name, description = description, created_at = time, updated_at = time)
    query.save()
    return redirect("/")

def question(request):
    request.session['course_id'] = request.POST['id']
    courses = models.Course.objects.all().get(pk = request.session['course_id'])
    context = {'courses' : courses}
    return render(request, "courses/delete.html", context)

def remove(request):
    models.Course.objects.all().get(pk = request.session['course_id']).delete()
    return redirect("/")
