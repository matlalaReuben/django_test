from django.shortcuts import render

import pyrebase
# pip install Pyrebase


config = {
	'apiKey' : "AIzaSyCZUMP0zqq9-taMYJmZNh-9aFNiKjDaFXA",
    'authDomain' : "cryptoportal-7b3d0.firebaseapp.com",
    'databaseURL' : "https://cryptoportal-7b3d0.firebaseio.com",
    'projectId' : "cryptoportal-7b3d0",
    'storageBucket' : "cryptoportal-7b3d0.appspot.com",
    'messagingSenderId' : "480280383856",
    'appId' : "1:480280383856:web:ab754bd484a755ef"
}


firebase = pyrebase.initialize_app( config );

database = firebase.database()

value = database.child("users")

print( "value : ", value, "value.val() : ", value.val())

# Create your views here.
from django.views.generic import TemplateView


class HomePageView(TemplateView):
	template_name = 'home.html'

class AboutPageView(TemplateView):
	template_name = 'about.html'
	
class AddCourseView(TemplateView):
	template_name = 'add_course.html'