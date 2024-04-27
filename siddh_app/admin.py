from django.contrib import admin
from siddh_app.models import Student, Faculty, College, Course, Program, ProgramCourse, Marks

# Register your models here.
admin.site.register(Faculty)
admin.site.register(Student)
admin.site.register(College)
admin.site.register(Course)
admin.site.register(Program)
admin.site.register(ProgramCourse)
admin.site.register(Marks)


