import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Course

def create_course(course_name, days):
    """
    Create a course with the given `course_name` and created the
    given number of `days` offset to now (negative for courses created
    in the past, positive for courses that have yet to be created).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Course.objects.create(course_name=course_name, created_at=time)

class CourseModelTests(TestCase):
    def test_no_courses(self):
        """
        If no courses exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('registration:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No courses are available.")
        self.assertQuerysetEqual(response.context['latest_course_list'], [])

    def test_past_course(self):
        """
        Courses with a created_at in the past are displayed on the
        index page.
        """
        create_course(course_name="Past course.", days=-30)
        response = self.client.get(reverse('registration:index'))
        self.assertQuerysetEqual(
            response.context['latest_course_list'],
            ['<Course: Past course.>']
        )
    def test_was_created_recently_with_future_course(self):
        """
        was_created_recently() returns False for courses whose created_at
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_course = Course(created_at=time)
        self.assertIs(future_course.was_created_recently(), False)

    def test_was_created_recently_with_recent_course(self):
        """
        was_published_recently() returns True for courses whose created_at
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_course = Course(created_at=time)
        self.assertIs(recent_course.was_created_recently(), True)

class CourseDetailViewTests(TestCase):
    def test_future_course(self):
        """
        The detail view of a course with a created_at in the future
        returns a 404 not found.
        """
        future_course = create_course(course_name='Future course.', days=5)
        url = reverse('registration:detail', args=(future_course.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        """
        The detail view of a course with a created_at in the past
        displays the course's text.
        """
        past_course = create_course(course_name='Past course.', days=-5)
        url = reverse('registration:detail', args=(past_course.id,))
        response = self.client.get(url)
        self.assertContains(response, past_course.course_name)