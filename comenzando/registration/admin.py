from django.contrib import admin

from .models import Course, Student


class StudentInline(admin.TabularInline):
    model = Student
    extra = 1

class CourseAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['course_name']}),
        ('Date information', {'fields': ['created_at']}),
    ]
    inlines = [StudentInline]
    list_display = ('course_name', 'created_at', 'was_created_recently')
    list_filter = ['created_at']
    search_fields = ['course_name']

admin.site.register(Course, CourseAdmin)
admin.site.register(Student)
