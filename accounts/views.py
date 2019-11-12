from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomCreationForm, CustomChangeForm
from .models import MyCustomUser
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import DetailView

# Create your views here.
class SignUpView(CreateView):
	form_class = CustomCreationForm
	success_url = reverse_lazy('login')
	template_name = 'signup.html'

class UserUpdateView(LoginRequiredMixin,UpdateView):
	model = MyCustomUser
	fields = ['username','email','first_name', 'last_name', 'stdno']
	template_name = 'user_update_form.html'

class UserDetailView(LoginRequiredMixin,DetailView):
	model = MyCustomUser
	template_name = 'user_details.html'
	
	
class AddCourseView():
	template_name = 'add_course.html'


def test_login(request):

	if request.method == 'POST' or request.method == 'post':
		print( "request.method == POST" )
		username_value = request.POST.get("username")
		password_value = request.POST.get("password")
		print( "username_value :", username_value, "password_value :", password_value )
	
	elif request.method == 'get' or request.method == 'GET':
		print("method is get" )
		username_value = request.GET.get("username")
		password_value = request.GET.get("password")
		print( "username_value :", username_value, "password_value :", password_value )

	else:
		print( "something went wrong !!!" )

	return render(request, 'registration/login.html' )

def test_register(request):
	if request.method == 'POST' or request.method == 'post':
		print( "request.method == POST" )
		username_value = request.POST.get("username")
		password_value = request.POST.get("password")
		c_password_value = request.POST.get("c_password")
		print( "username_value :", username_value, "password_value :", password_value, "c_password :", c_password )
	
	elif request.method == 'get' or request.method == 'GET':
		print("method is get" )
		username_value = request.GET.get("username")
		password_value = request.GET.get("password")
		c_password_value = request.GET.get("c_password")

		print( "username_value :", username_value, "password_value :", password_value, "c_password", c_password )

	else:
		print( "something went wrong !!!" )

	return render(request, 'templates/signup.html' )

