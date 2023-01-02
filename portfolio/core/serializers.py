from rest_framework import serializers
from .models import (Userdetailmodel, Usersociallink, Aboutcontent,
                     Experience, Experienceinput, Projecttool, Project, Blog)


class UserdetailmodelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userdetailmodel
        fields = '__all__'


class UsersociallinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usersociallink
        fields = '__all__'


class AboutcontentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aboutcontent
        fields = '__all__'


class ExperienceinputSerializer(serializers.ModelSerializer):
    experience = serializers.CharField(read_only=True)
    experience_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Experienceinput
        fields = '__all__'


class ExperienceSerializer(serializers.ModelSerializer):
    experience_inputs = ExperienceinputSerializer(many=True, read_only=True)

    class Meta:
        model = Experience
        fields = '__all__'


class ProjecttoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projecttool
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    tool = ProjecttoolSerializer(many=True, read_only=False)

    class Meta:
        model = Project
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
