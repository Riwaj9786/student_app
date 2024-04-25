from django.shortcuts import render
from siddh_app.models import Student
from django.views.generic import (TemplateView)

# Create your views here.
class StudentRecord(TemplateView):
    template_name = 'siddh_app/index.html'
    model = Student

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['students'] = Student.objects.all()
        return context