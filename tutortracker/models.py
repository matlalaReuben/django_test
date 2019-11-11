from django.db import models

# Create your models here.


class Course(models.Model):
	course_code = models.CharField( unique=True, max_length=10 )
	course_name = models.CharField( unique=True, max_length=100 )
	course_owner_username = models.CharField( max_length=50)
	
	
	
# class User(models.model):
	# username
	# type = 


