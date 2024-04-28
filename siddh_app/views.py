from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from siddh_app.forms import StudentForm, MarksUpdateForm
from siddh_app.models import Student, College, Faculty, Program, Mark, Semester
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


def update_all_marks(request, student_id, program_id, semester_id):
    student = get_object_or_404(Student, pk = student_id)
    program = get_object_or_404(Program, pk = program_id)
    semester = get_object_or_404(Semester, pk = semester_id)

    marks = Mark.objects.filter(student = student, course__program = program, course__programcourse__semester = semester)

    if request.method == "POST":
        for mark in marks:
            mark_value = request.POST.get('course_{}_mark'.format(mark.course.id))
            mark.mark = mark_value
            mark.save()

        return HttpResponseRedirect('success/')
    
    return render(request, 'update_all_marks.html', {'student': student, 'program': program, 'semester': semester, 'marks': marks})
