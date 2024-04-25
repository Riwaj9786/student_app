from django.urls import path
from siddh_app import views

app_name = 'siddh_app'

urlpatterns = [
    path('', views.home, name='home'),    
]