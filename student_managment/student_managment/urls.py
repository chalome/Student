
from django.contrib import admin
from django.urls import path,include
from account.views import home
from django.conf import settings
from django.conf.urls.static import static
from student.views import (
    HomeView,StudentListView,StudentCreateView,
    StudentDetailView,StudentUpdateView,StudentDeleteView,StudentViewSet)
from account.views import CustomLoginView,SingUpView,CustomLogoutView,CustomUserViewSet
from rest_framework import routers
from rest_framework.routers import DefaultRouter


# router=routers.SimpleRouter()
# router.register('student',StudentViewSet,basename='student')
router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'users', CustomUserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/home', home.as_view(),name='account_home'),
    path('student/home', HomeView.as_view(),name='home_student'),
    path('student/list', StudentListView.as_view(),name='student_list'),
    path('student/add', StudentCreateView.as_view(),name='student_add'),
    path('student/detail/<int:pk>', StudentDetailView.as_view(),name='student_detail'),
    path('student/update/<int:student_id>', StudentUpdateView.as_view(),name='student_update'),
    path('student/delete/<int:student_id>', StudentDeleteView.as_view(),name='student_delete'),
    path('', CustomLoginView.as_view(),name='login'),
    path('account/signup', SingUpView.as_view(),name='signup'),
    path('logout/', CustomLogoutView.as_view(),name='logout'),

    path('api/',include(router.urls)),
    # path('api/student_list/', StudentViewSet.as_view({'get': 'list'}),name='student-list'),
]
if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)