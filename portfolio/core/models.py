from django.db import models

# Create your models here.
from django.db import models
from cloudinary_storage.storage import RawMediaCloudinaryStorage
from portfolio.commons.models import BaseModel



class Userdetailmodel(BaseModel):
	welcome_title = models.CharField(null=False, blank=False, max_length=100)
	welcome_note = models.CharField(null=False, blank=False, max_length=255)
	welcome_description = models.TextField(null=False, blank=False, max_length=500)
	cv_file = models.FileField(upload_to='raw/', blank=True, storage=RawMediaCloudinaryStorage())
	user_image = models.ImageField(null=False, blank=False, upload_to='images', max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self) -> str:
		return super().__str__()
	



class Usersociallink(BaseModel):
	name = models.CharField(max_length=50)
	link = models.TextField(max_length=50)
	icon = models.ImageField(upload_to='icons')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self) -> str:
		return super().__str__() + self.name



class Aboutcontent(BaseModel):
	paragraph = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self) -> str:
		return super().__str__() 



class Experience(BaseModel):
	image = models.ImageField(upload_to='experience')
	name = models.CharField(max_length=255)
	title = models.CharField(max_length=255)
	start = models.CharField(max_length=50)
	end = models.CharField(max_length=50)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self) -> str:
		return super().__str__() + self.name



class Experienceinput(BaseModel):
	content = models.TextField()
	experience = models.ForeignKey('Experience', on_delete=models.CASCADE, related_name='experience_inputs')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self) -> str:
		return super().__str__() + self.experience

class Projecttool(BaseModel):
	name = models.CharField(unique=True, max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self) -> str:
		return self.name


class Project(BaseModel):
	title = models.CharField(max_length=255)
	about = models.CharField(max_length=255)
	tool = models.ManyToManyField('Projecttool', related_name='project_tools')
	cover = models.ImageField(upload_to='cover')
	link = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)



class Blog(BaseModel):
	title = models.CharField(unique=True, max_length=255)
	cover = models.ImageField(upload_to='cover')
	link = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

