from django.urls import path
from siddh_app import views

urlpatterns = [
    path('', views.home, name='home'),    
]