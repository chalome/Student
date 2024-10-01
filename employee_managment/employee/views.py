from rest_framework.views import APIView
from .models import Service,Category,Employee
from .serializers import (CategoryDetailSerializer,CategoryListSerializer,
                          ServiceDetailSerializer,ServiceListSerializer,
                          EmployeeSerializer)
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
from rest_framework.decorators import action

class MultipleSerializerMixin:
	detail_serializer_class=None
	
	def get_serializer_class(self):
		if self.action=='retrieve' and self.detail_serializer_class is not None:
			return self.detail_serializer_class
		return super().get_serializer_class()

class CategoryViewSet(ReadOnlyModelViewSet):
	serializer_class=CategoryListSerializer
	detail_serializer_class=CategoryDetailSerializer
	def get_queryset(self):
		return Category.objects.all()
	def get_serializer_class(self):
		if self.action=='retrieve':
			return self.detail_serializer_class
		return super().get_serializer_class()

# class ServiceApiView(APIView):
# 	def get(self,*args,**kwargs):
# 		services=Service.objects.all()
# 		serializer=ServiceSerializer(services,many=True)
# 		return Response(serializer.data)

class ServiceViewSet(MultipleSerializerMixin,ModelViewSet):
    detail_serializer_class=ServiceDetailSerializer
    serializer_class=ServiceListSerializer
    
    def get_queryset(self):
        return Service.objects.filter(active=True)
    
    @action(detail=True, methods=['post'])
    def disable(self, request, pk):
        self.get_object().disable()
        return Response()
    
		
class EmployeeViewSet(ModelViewSet):
	serializer_class=EmployeeSerializer
	def get_queryset(self):
		queryset=Employee.objects.filter(working=True)
		service_id=self.request.GET.get('service_id')
		if service_id is not None:
			queryset=queryset.filter(service_id=service_id)
		return queryset