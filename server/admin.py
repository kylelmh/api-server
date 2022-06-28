from django.contrib import admin
from django.apps import apps
from server.models import *

# Register remaining models
server = apps.get_app_config('server')
for model in server.get_models():  
  try:
    admin.site.register(model)
  except admin.sites.AlreadyRegistered:
    pass