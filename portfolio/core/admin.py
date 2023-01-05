from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import (SkillCategory,Skills, Userdetailmodel, Usersociallink, Aboutcontent, Experience, Experienceinput, Projecttool, Project, Blog)


admin.site.register(
	(Userdetailmodel,Experienceinput, Usersociallink, Projecttool, Project, Blog )
)
DEFAULT_READONLY_FIELDS = ("created_at","updated_at","created_by","updated_by")
class ProfileInline(admin.TabularInline):
	model = Userdetailmodel
	readonly_fields = DEFAULT_READONLY_FIELDS
	extra = 1

@admin.register(Aboutcontent)
class AboutAdmin(admin.ModelAdmin):
	inline = [
	ProfileInline
	]

class ExperienceinputInline(admin.StackedInline):
    model = Experienceinput
    extra = 2
@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    exclude =  DEFAULT_READONLY_FIELDS
    inlines = [
        ExperienceinputInline,
    ]


# Skills
class SkillsInline(admin.TabularInline):
    model = Skills
    extra = 3

@admin.register(Skills)
class SkillAdmin(admin.ModelAdmin):
	model = Skills
	exclude = DEFAULT_READONLY_FIELDS

@admin.register(SkillCategory)
class CategoryAdmin(admin.ModelAdmin):
    exclude = DEFAULT_READONLY_FIELDS
    inlines = [
        SkillsInline,
		
    ]
