from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (UserdetailmodelView, UsersociallinkView, AboutcontentView, ExperienceView, ExperienceinputView, ProjecttoolView, ProjectView, BlogView)


router = DefaultRouter()
router.register('userdetailmodel', UserdetailmodelView, basename='userdetailmodel')
router.register('usersociallink', UsersociallinkView, basename='usersociallink')
router.register('aboutcontent', AboutcontentView, basename='aboutcontent')
router.register('experience', ExperienceView, basename='experience')
router.register('experienceinput', ExperienceinputView, basename='experienceinput')
router.register('projecttool', ProjecttoolView, basename='projecttool')
router.register('project', ProjectView, basename='project')
router.register('blog', BlogView, basename='blog')

urlpatterns = [
	path('', include(router.urls)),
]
