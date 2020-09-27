from django.db import models


class Course(models.Model):
    course_name = models.CharField(max_length=200)
    created_at = models.DateTimeField('course created')
    def __str__(self):
        return self.course_name


class Student(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=200)
    student_likes = models.IntegerField(default=0)
    def __str__(self):
        return self.student_name
    