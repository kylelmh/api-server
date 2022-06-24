from ctypes import Array
from django.contrib import admin
from django.apps import apps
from django.forms import Textarea
from server.models import *
from django.contrib.postgres.fields import ArrayField

server = apps.get_app_config('server')
# Register your models here.
for model in server.get_models():  
  try:
    admin.site.register(model)
  except admin.sites.AlreadyRegistered:
    pass