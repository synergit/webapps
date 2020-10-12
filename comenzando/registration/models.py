import datetime

from django.db import models
from django.utils import timezone


class Course(models.Model):
    course_name = models.CharField(max_length=200)
    created_at = models.DateTimeField('course created')
    def was_created_recently(self):
        return timezone.now() >= self.created_at >= timezone.now() - datetime.timedelta(days=1)
    was_created_recently.admin_order_field = 'created_at'
    was_created_recently.boolean = True
    was_created_recently.short_description = 'Created recently?'

    def __str__(self):
        return self.course_name


class Student(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=200)
    student_likes = models.IntegerField(default=0)
    def __str__(self):
        return self.student_name
    