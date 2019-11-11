from django.urls import path

from .views import HomePageView, AboutPageView, AddCourseView

urlpatterns = [
    path('tutortracker/', HomePageView.as_view(), name='home'),
    path('tutortracker/about/', AboutPageView.as_view(), name = 'about'),
    path('tutortracker/add_course', AddCourseView.as_view(), name='add_course'),
]
