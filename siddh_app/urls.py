from django.urls import path
from siddh_app import views

app_name = 'siddh_app'

urlpatterns = [
    path('', views.StudentRecord.as_view(), name='studentrecord'),   
    path('student/new/', views.CreateStudentView.as_view(), name='create_student'), 
]