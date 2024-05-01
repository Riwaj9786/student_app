from django.urls import path
from siddh_app import views

app_name = 'siddh_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('student/', views.StudentRecord.as_view(), name='studentrecord'),
    path('program/', views.ProgramRecord.as_view(), name='programrecord'),   
    path('student/new/', views.CreateStudentView.as_view(), name='create_student'),
    path('program/new/', views.CreateProgramView.as_view(), name='create_program'),
    # path('marks/update/', views.update_all_marks, name='update_marks'), 
]