from django.http import HttpResponse
from django.template import loader

from .models import Course

def index(request):
    # return HttpResponse("Hello, world. You're at the registration index.")
    # latest_course_list = Course.objects.order_by('-created_at')[:5]
    latest_course_list = Course.objects.order_by('-created_at')[:5]
    for a in latest_course_list:
        print(a.id, a.course_name, a.created_at) 
    template = loader.get_template('registration/index.html')
    # print(type(template))
    context = {
        'latest_course_list':latest_course_list,
    }
    # output = ', '.join([c.course_name for c in latest_course_list])
    return HttpResponse(template.render(context, request))


def detail(request, course_id):
    return HttpResponse("You're looking at course %s." % course_id)

def results(request, course_id):
    response = "You're looking at the students of course %s."
    return HttpResponse(response % course_id)

def register(request, course_id):
    return HttpResponse("You're registering on course %s." % course_id)