from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DetailView,DeleteView
from student.models import Student
from student.forms import StudentForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from student.serializers import StudentSerializer
from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

class HomeView(TemplateView):
	template_name='student/home.html'

class StudentListView(LoginRequiredMixin,ListView):
	model=Student
	template_name='student/student_list.html'

	# def get_queryset(self):
	# 	return Student.objects.all()

class StudentCreateView(LoginRequiredMixin,CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'student/AddStudent.html'
    success_url = reverse_lazy('student_list')

    def get(self, request):
        form = self.get_form()
        message = ''
        return render(request,self.template_name,context={'form': form, 'message': message})

    def post(self, request):
        form = self.form_class(request.POST,request.FILES)
        if form.is_valid():
        	form.save()
        	return redirect(self.success_url)
        message='Error'
        return render(request,self.template_name,context={'form': form, 'message': message})

class StudentDetailView(LoginRequiredMixin,DetailView):
 	model=Student
 	template_name='student/student_detail.html'
 	context_object_name='student'

class StudentUpdateView(LoginRequiredMixin,UpdateView):
	model=Student
	form_class=StudentForm
	template_name='student/student_update.html'
	success_url=reverse_lazy('student_list')

	def get_object(self,queryset=None):
		return get_object_or_404(Student,id=self.kwargs['student_id'])

class StudentDeleteView(LoginRequiredMixin,DeleteView):
	model=Student
	template_name='student/student_delete.html'
	context_object_name='student'
	success_url=reverse_lazy('student_list')

	def get_object(self,queryset=None):
		return get_object_or_404(Student,id=self.kwargs['student_id'])

# class StudentViewSet(ModelViewSet):
# 	serializer_class=StudentSerializer

# 	def get_queryset(self):
# 		return Student.objects.all()
class StudentViewSet(LoginRequiredMixin, ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        student = self.get_object()
        serializer = self.get_serializer(student)
        return Response(serializer.data)

    def update(self, request, pk=None):
        student = self.get_object()
        serializer = self.get_serializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        student = self.get_object()
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''
StudentViewSet Class
The StudentViewSet class is a subclass of viewsets.ModelViewSet, which provides default implementations
 for common CRUD operations. Here’s a breakdown of each method:

Copy
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
queryset: This attribute defines the set of Student instances that the viewset will operate on. 
It retrieves all student records from the database.
serializer_class: This specifies the serializer to be used for converting model instances to 
JSON format and vice versa.
1. list
Copy
def list(self, request):
    queryset = self.get_queryset()
    serializer = self.get_serializer(queryset, many=True)
    return Response(serializer.data)
Purpose: This method handles GET requests to retrieve a list of all students.

Functionality:

self.get_queryset(): Calls the inherited method to retrieve the queryset defined in the viewset 
(all Student instances).
self.get_serializer(queryset, many=True): Serializes the queryset. The many=True argument indicates 
that multiple instances are being serialized.
Response(serializer.data): Returns a response containing the serialized data in JSON format.
2. create
Copy
def create(self, request):
    serializer = self.get_serializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
Purpose: This method handles POST requests to create a new student.

Functionality:

self.get_serializer(data=request.data): Initializes the serializer with the incoming data from the request.
serializer.is_valid(): Validates the data against the serializer's rules (e.g., required fields, data types).
serializer.save(): If the data is valid, this method saves the new student instance to the database.
Response(serializer.data, status=status.HTTP_201_CREATED): Returns the serialized data of the newly 
created student with a 201 Created status.
If the data is not valid, it returns the validation errors with a 400 Bad Request status.
3. retrieve
Copy
def retrieve(self, request, pk=None):
    student = self.get_object()
    serializer = self.get_serializer(student)
    return Response(serializer.data)
Purpose: This method handles GET requests for a specific student identified by the primary key (pk).

Functionality:

self.get_object(): Retrieves the specific Student instance based on the pk provided in the URL.
 If the object does not exist, it raises a 404 Not Found error automatically.
self.get_serializer(student): Serializes the retrieved student instance.
Response(serializer.data): Returns the serialized data of the specific student in JSON format.
4. update
Copy
def update(self, request, pk=None):
    student = self.get_object()
    serializer = self.get_serializer(student, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
Purpose: This method handles PUT requests to update an existing student.

Functionality:

self.get_object(): Retrieves the specific Student instance to be updated.
self.get_serializer(student, data=request.data): Initializes the serializer with the existing 
student instance and the new data from the request.
serializer.is_valid(): Validates the new data against the serializer's rules.
serializer.save(): If valid, updates the existing student instance in the database.
Response(serializer.data): Returns the updated serialized data.
If the data is not valid, it returns the validation errors with a 400 Bad Request status.
5. destroy
Copy
def destroy(self, request, pk=None):
    student = self.get_object()
    student.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
Purpose: This method handles DELETE requests to remove a specific student.

Functionality:

self.get_object(): Retrieves the specific Student instance to be deleted.
student.delete(): Deletes the retrieved student instance from the database.
Response(status=status.HTTP_204_NO_CONTENT): Returns a response with a 204 No Content status,
 indicating that the deletion was successful and there is no content to return.
Summary of Functionality
CRUD Operations: The StudentViewSet provides a complete set of CRUD operations for managing Student records:

List: Retrieve all students.
Create: Add a new student.
Retrieve: Get details of a specific student.
Update: Modify an existing student.
Destroy: Remove a student.
Automatic Handling of Errors: The viewset automatically handles common errors, such as 
returning a 404 error if a requested student does not exist, and returning validation errors 
for invalid input.
'''