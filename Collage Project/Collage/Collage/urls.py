"""
URL configuration for Collage project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1.views import home,department,dele_Dept,update_Dept,hod,delete_Hod,update_Hod,professor,delete_professor,update_professor,student,delete_Stud,update_student

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home, name= 'home'),
    #################################################################
    path('dept', department, name='department'),
    path('dept/delete/<int:pk>/',dele_Dept, name='deleteDept'),
    path('dept/update/<int:pk>/',update_Dept, name='updateDept'),
    ###################################################################
    path('hod',hod, name='hod'),
    path('hod/delete/<int:pk>/',delete_Hod, name='deleteHod'),
    path('hod/update<int:pk>/',update_Hod, name='updateHod'),
    ###################################################################
    path('professor',professor, name='professor'),
    path('professor/update/<int:pk>/',update_professor, name='updateProfessor'),
    path('professor/delete/<int:pk>/',delete_professor, name='deleteProfessor'),

    ###############################################################################

    path('student',student, name='student'),
    path('student/delete/<int:pk>',delete_Stud,name='deleteStudent'),
    path('student/update/<int:pk>/',update_student, name='updateStudent'),




]
