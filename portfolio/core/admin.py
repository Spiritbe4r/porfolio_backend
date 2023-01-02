from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import (Userdetailmodel, Usersociallink, Aboutcontent, Experience, Experienceinput, Projecttool, Project, Blog)


admin.site.register(
	(Userdetailmodel, Usersociallink, Aboutcontent, Experience, Experienceinput, Projecttool, Project, Blog)
)
