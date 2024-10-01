
from django.contrib import admin
from django.urls import path,include
from employee.views import EmployeeViewSet,CategoryViewSet,ServiceViewSet
from rest_framework import routers

router=routers.SimpleRouter()
router.register('employee', EmployeeViewSet,basename='employee')
router.register('category', CategoryViewSet,basename='category')
router.register('service', ServiceViewSet,basename='service')

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    #path('api/category/', CategoryViewSet.as_view()),
    # path('api/service/', ServiceApiView.as_view()),
]
