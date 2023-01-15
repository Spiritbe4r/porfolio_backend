from django.db import models

# Create your models here.
from django.db import models
from cloudinary_storage.storage import RawMediaCloudinaryStorage
from portfolio.commons.models import BaseModel


class Userdetailmodel(BaseModel):
    welcome_title = models.CharField(null=False, blank=False, max_length=100)
    welcome_note = models.CharField(null=False, blank=False, max_length=255)
    welcome_description = models.TextField(
        null=False, blank=False, max_length=1000)
    cv_file = models.FileField(
        upload_to='raw/', blank=True, storage=RawMediaCloudinaryStorage())
    user_image = models.ImageField(
        null=False, blank=False, upload_to='images', max_length=255)


    class Meta:
        verbose_name = "UserDetail"
        verbose_name_plural = "UserDetails"

    def __str__(self) -> str:
        return self.welcome_title


class Usersociallink(BaseModel):
    name = models.CharField(max_length=50)
    link = models.TextField(max_length=50)
    icon = models.ImageField(upload_to='icons')


    class Meta:
        verbose_name = "UserSocialLink"
        verbose_name_plural = "UserSocialLinks"

    def __str__(self) -> str:
        return self.name
	


class Aboutcontent(BaseModel):
    paragraph = models.TextField()

    def __str__(self) -> str:
        return super().__str__()


class Experience(BaseModel):
    image = models.ImageField(upload_to='experience')
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    start = models.CharField(max_length=50)
    end = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Experience"
        verbose_name_plural = "Experiences"

    def __str__(self) -> str:
        return self.name


class Experienceinput(BaseModel):
    content = models.TextField()
    experience = models.ForeignKey(
        'Experience', on_delete=models.CASCADE, related_name='experience_inputs')

    def __str__(self) -> str:
        return super().__str__()


class Projecttool(BaseModel):
    name = models.CharField(unique=True, max_length=100)
    image = models.ImageField(
        null=False, blank=False, upload_to='images', max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Project(BaseModel):
    title = models.CharField(max_length=255)
    about = models.CharField(max_length=255)
    tool = models.ManyToManyField('Projecttool', related_name='project_tools')
    cover = models.ImageField(upload_to='cover')
    link = models.TextField()

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self) -> str:
        return self.title


class Blog(BaseModel):
    title = models.CharField(unique=True, max_length=255)
    cover = models.ImageField(upload_to='cover')
    link = models.TextField()

    def __str__(self) -> str:
        return self.title

# SKILLS SECTION


class SkillCategory(BaseModel):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=255)
    image = models.ImageField(
        null=False, blank=False, upload_to='images', max_length=255)

    class Meta:
        verbose_name = 'SkillCategory'
        verbose_name_plural = 'SkillCategorys'

    def __str__(self):
        return self.name


class Skills(BaseModel):
    category = models.ForeignKey(SkillCategory,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'
	
    def __str__(self):
        return self.name
