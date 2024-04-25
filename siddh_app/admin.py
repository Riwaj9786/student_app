from django.contrib import admin
from siddh_app.models import Student, Faculty, Registration

# Register your models here.
admin.site.register(Faculty)
admin.site.register(Student)
admin.site.register(Registration)
