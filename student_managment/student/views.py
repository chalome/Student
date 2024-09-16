from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DetailView,DeleteView
from student.models import Student
from student.forms import StudentForm
from django.urls import reverse_lazy
class HomeView(TemplateView):
	template_name='student/home.html'

class StudentListView(ListView):
	model=Student
	template_name='student/student_list.html'

	# def get_queryset(self):
	# 	return Student.objects.all()

class StudentCreateView(CreateView):
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

class StudentDetailView(DetailView):
 	model=Student
 	template_name='student/student_detail.html'
 	context_object_name='student'

class StudentUpdateView(UpdateView):
	model=Student
	form_class=StudentForm
	template_name='student/student_update.html'
	success_url=reverse_lazy('student_list')

	def get_object(self,queryset=None):
		return get_object_or_404(Student,id=self.kwargs['student_id'])

class StudentDeleteView(DeleteView):
	model=Student
	template_name='student/student_delete.html'
	context_object_name='student'
	success_url=reverse_lazy('student_list')

	def get_object(self,queryset=None):
		return get_object_or_404(Student,id=self.kwargs['student_id'])


