"""
URL configuration for student_managment project.

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
from account.views import home
from student.views import HomeView,StudentListView,StudentCreateView,StudentDetailView,StudentUpdateView,StudentDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/home', home.as_view(),name='home_account'),
    path('student/home', HomeView.as_view(),name='home_student'),
    path('student/list', StudentListView.as_view(),name='student_list'),
    path('student/add', StudentCreateView.as_view(),name='student_add'),
    path('student/detail/<int:pk>', StudentDetailView.as_view(),name='student_detail'),
    path('student/update/<int:student_id>', StudentUpdateView.as_view(),name='student_update'),
    path('student/delete/<int:student_id>', StudentDeleteView.as_view(),name='student_delete'),
]
