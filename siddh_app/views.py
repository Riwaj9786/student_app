from django.shortcuts import render
from siddh_app.forms import StudentForm
from siddh_app.models import Student, College, Faculty, Program
from django.views.generic import (TemplateView,
                                  CreateView)

# Create your views here.
class StudentRecord(TemplateView):
    template_name = 'siddh_app/index.html'
    model = Student

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['students'] = Student.objects.all().order_by('-batch_year')
        return context
    

class CreateStudentView(CreateView):
    fields = ('batch_year', 'first_name', 'middle_name', 'last_name', 'gender', 'do_birth', 'email_add', 'program', 'faculty', 'college', 'semester')
    model = Student


class CreateProgramView(CreateView):
    fields = ('__all__')
    model = Program