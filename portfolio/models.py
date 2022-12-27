from django.db import models


class Userdetailmodel(models.Model):
	welcome_title = models.CharField(null=False, blank=False, max_length=100)
	welcome_note = models.CharField(null=False, blank=False, max_length=255)
	welcome_description = models.TextField(null=False, blank=False, max_length=255)
	cv_link = models.TextField(null=False, blank=False, max_length=255)
	user_image = models.ImageField(null=False, blank=False, upload_to='images', max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)



class Usersociallink(models.Model):
	name = models.CharField(max_length=50)
	link = models.TextField(max_length=50)
	icon = models.ImageField(upload_to='icons')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)



class Aboutcontent(models.Model):
	paragraph = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)



class Experience(models.Model):
	image = models.ImageField(upload_to='experience')
	name = models.CharField(max_length=255)
	title = models.CharField(max_length=255)
	start = models.CharField(max_length=50)
	end = models.CharField(max_length=50)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)



class Experienceinput(models.Model):
	content = models.TextField()
	experience = models.ForeignKey('Experience', on_delete=models.CASCADE, related_name='experience_inputs')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)



class Projecttool(models.Model):
	name = models.CharField(unique=True, max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)



class Project(models.Model):
	title = models.CharField(max_length=255)
	about = models.CharField(max_length=255)
	tool = models.ManyToManyField('Projecttool', related_name='project_tools')
	cover = models.ImageField(upload_to='cover')
	link = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)



class Blog(models.Model):
	title = models.CharField(unique=True, max_length=255)
	cover = models.ImageField(upload_to='cover')
	link = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

