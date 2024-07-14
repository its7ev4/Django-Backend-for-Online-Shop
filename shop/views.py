from django.shortcuts import render # type: ignore
from django.http import HttpResponse # type: ignore
from django.http import Http404 # type: ignore
from .models import Course



def index(request):
    courses = Course.objects.all()
    return render(request, 'shop/courses.html', {'courses':courses})

def single_course(request, course_id):
    try:
        course = Course.objects.get(pk=course_id)
        return render(request, 'shop/single_course.html', {'course':course})
    except Course.DoesNotExist:
        raise Http404()