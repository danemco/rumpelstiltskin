from django.contrib import admin
from timeclock.models import Record, Project

class RecordAdmin(admin.ModelAdmin):
    pass

class ProjectAdmin(admin.ModelAdmin):
    pass

admin.site.register(Record, RecordAdmin)
admin.site.register(Project, ProjectAdmin)

