from django.urls import path



from . import views
from .views import HomePageView, AboutPageView, AddCourseView, ForumView


urlpatterns = [
    path('tutortracker/', HomePageView.as_view(), name='home'),
    path('tutortracker/about/', AboutPageView.as_view(), name = 'about'),
    path('tutortracker/add_course', AddCourseView.as_view(), name='add_course'),
    path('tutortracker/forum', ForumView.as_view(), name='forum'),
    path('tutortracker/test_click', views.test_click , name='test_click	'),
]
