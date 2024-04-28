from django import forms
from siddh_app.models import Student, Faculty, Mark

class StudentForm(forms.ModelForm):

    class Meta():
        model = Student
        fields = ('batch_year', 'first_name', 'middle_name', 'last_name', 'do_birth', 'gender', 'faculty', 'semester')

        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),  # Use DateInput widget with type='date'
            'text': forms.TextInput(attrs={'class': 'textinputclass'}),
        }



class MarksUpdateForm(forms.ModelForm):
    class Meta:
        model = Mark
        fields = ['marks']