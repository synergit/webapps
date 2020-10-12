from django.http import HttpResponseRedirect
from django.utils import timezone
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Course, Student

class IndexView(generic.ListView):
    template_name = 'registration/index.html'
    context_object_name = 'latest_course_list'

    def get_queryset(self):
        return Course.objects.filter(
                created_at__lte=timezone.now()
            ).order_by('-created_at')[:5]

class DetailView(generic.DetailView):
    model = Course
    template_name = 'registration/detail.html'

    def get_queryset(self):
        """
        Excludes any courses that aren't published yet.
        """
        return Course.objects.filter(created_at__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Course
    template_name = 'registration/results.html'

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
