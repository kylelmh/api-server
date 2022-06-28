from django.contrib import admin
from django.apps import apps
from server.models import *

# Custom admin displays
@admin.register(Employment)
class EmploymentAdmin(admin.ModelAdmin):
    list_display = ('skill_tags', 'get_skill_tags')
    search_fields = ('skill_tags',)

    def get_skill_tags(self, obj):
        return obj.bars.all()

# Register remaining models
server = apps.get_app_config('server')
for model in server.get_models():  
  try:
    admin.site.register(model)
  except admin.sites.AlreadyRegistered:
    pass