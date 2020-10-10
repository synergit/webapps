from django.http import HttpResponse
# from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.template import loader

from .models import Course

def index(request):
    latest_course_list = Course.objects.order_by('-created_at')[:5]
    context = {
        'latest_course_list':latest_course_list,
    }
    return render(request, 'registration/index.html', context)


def detail(request, course_id):
    # return HttpResponse("You're looking at course %s." % course_id)
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'registration/detail.html', {'course': course})

def results(request, course_id):
    response = "You're looking at the students of course %s."
    return HttpResponse(response % course_id)

def register(request, course_id):
    return HttpResponse("You're registering on course %s." % course_id)