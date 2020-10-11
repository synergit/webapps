from django.http import HttpResponse, HttpResponseRedirect
# from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.urls import reverse

from .models import Course, Student

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
    # response = "You're looking at the students of course %s."
    # return HttpResponse(response % course_id)
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'registration/results.html', {'course': course})

def like(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    # return HttpResponse("You like on student %s." % student_id)
    try:
        selected_student = course.student_set.get(pk=request.POST['student'])
    except (KeyError, Student.DoesNotExist):
        # Redisplay the question liking form.
        return render(request, 'registration/detail.html', {
            'course': course,
            'error_message': "You didn't select a student.",
        })
    else:
        selected_student.student_likes += 1
        selected_student.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('registration:results', args=(course.id,)))
        