from django.contrib import admin
from course.models import *

admin.site.register(Users)
admin.site.register(Course)
admin.site.register(CourseVideo)
admin.site.register(QueryForm)
admin.site.register(StudentCourseAttend)
admin.site.register(StudentAttendance)
