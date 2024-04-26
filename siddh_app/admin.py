from django.contrib import admin
from siddh_app.models import Student, Faculty, College, Course, Department

# Register your models here.
admin.site.register(Faculty)
admin.site.register(Student)
admin.site.register(College)
admin.site.register(Course)
admin.site.register(Department)



