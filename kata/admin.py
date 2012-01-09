from django.contrib import admin
from myweb.kata.models import Tasks, Projects

class TasksAdmin(admin.ModelAdmin):
	pass

class ProjectsAdmin(admin.ModelAdmin):
	pass
	
admin.site.register(Tasks, TasksAdmin)
admin.site.register(Projects, ProjectsAdmin)