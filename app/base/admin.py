from django.contrib import admin

from base.models import About, Experience, Message, Project, Skill, Tool

# Register your models here.
admin.site.register(About)
admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(Experience)
admin.site.register(Message)
admin.site.register(Tool)
