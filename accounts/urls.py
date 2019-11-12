from django.urls import path
from . import views
from .views import SignUpView, UserUpdateView , UserDetailView

urlpatterns = [
	path('signup/',SignUpView.as_view() , name = 'signup'),
	path('signup/test_register', views.test_register, name = 'test_register'),
	path('<int:pk>/update/',UserUpdateView.as_view(), name = 'update_user'),
	path('<int:pk>/',UserDetailView.as_view(), name = 'user_details'),
	path('login/test_login/', views.test_login, name = 'test_login')
]