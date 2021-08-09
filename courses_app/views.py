from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import Courses

def index(request): #GET REQUEST
    context = {
    "all_the_courses": Courses.objects.all(),
    }
    return render(request, "index.html", context)

def create_course(request): #POST REQUEST
    errors = Courses.objects.validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")
    elif request.method != "POST":
        return redirect("/")
    elif request.method == "POST":
        create = Courses.objects.create(name = request.POST["name"], description = request.POST["description"])
        course_id = create.id
        messages.success(request, "Course successfully created")
    return redirect("/")

def view_course(request, course_id): #GET REQUEST
    this_course = Courses.objects.get(id = course_id)
    context = {
    "a_course": this_course
    }
    return render(request, "view_course.html", context)

def delete_course(request, course_id): #POST Request
    if request.method != "POST":
        return redirect("/")
    if request.method == "POST":
        a_course = Courses.objects.get(id = course_id)
        a_course.delete()
    return redirect("/")