# EmplApp/urls.py
from django.urls import path, re_path
from . import views

urlpatterns = [
    
    path('department/', views.departmentApi, name='departmentApi'),
    path('employee/', views.employeeApi, name='employeeApi'),
    re_path(r'^employee/savefile$', views.SaveFile, name='savefile'),  
    re_path(r'^$', views.home),

]