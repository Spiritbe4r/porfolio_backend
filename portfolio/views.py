from rest_framework.viewsets import ModelViewSet
from myportfolio.utils import Helper
from .models import (Userdetailmodel, Usersociallink, Aboutcontent, Experience, Experienceinput, Projecttool, Project, Blog)
from .serializers import (UserdetailmodelSerializer, UsersociallinkSerializer, AboutcontentSerializer, ExperienceSerializer, ExperienceinputSerializer, ProjecttoolSerializer, ProjectSerializer, BlogSerializer)


class UserdetailmodelView(ModelViewSet):
	queryset = Userdetailmodel.objects.all()
	serializer_class = UserdetailmodelSerializer


class UsersociallinkView(ModelViewSet):
	queryset = Usersociallink.objects.all()
	serializer_class = UsersociallinkSerializer


class AboutcontentView(ModelViewSet):
	queryset = Aboutcontent.objects.all()
	serializer_class = AboutcontentSerializer


class ExperienceView(ModelViewSet):
	queryset = Experience.objects.all()
	serializer_class = ExperienceSerializer


class ExperienceinputView(ModelViewSet):
	queryset = Experienceinput.objects.all()
	serializer_class = ExperienceinputSerializer


class ProjecttoolView(ModelViewSet):
	queryset = Projecttool.objects.all()
	serializer_class = ProjecttoolSerializer


class ProjectView(ModelViewSet):
	queryset = Project.objects.all()
	serializer_class = ProjectSerializer


class BlogView(ModelViewSet):
	queryset = Blog.objects.all()
	serializer_class = BlogSerializer
