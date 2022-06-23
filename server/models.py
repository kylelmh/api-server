from django.contrib.auth.models import User
from django.db import models
from datetime import datetime
# Create your models here.

class TimestampedModel(models.Model):
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  class Meta:
    abstract = True

class Employment(TimestampedModel):
  start_date = models.DateField(default=datetime.now)
  end_date = models.DateField(default=datetime.now)
  position = models.JSONField(default=dict)
  status = models.CharField(max_length=255)
  company = models.JSONField(default=dict)
  description = models.JSONField(default=dict)
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class Education(TimestampedModel):
  start_date = models.DateField(default=datetime.now)
  end_date = models.DateField(default=datetime.now)
  school = models.JSONField(default=dict)
  faculty = models.JSONField(default=dict)
  department = models.JSONField(default=dict)
  description = models.JSONField(default=dict)
  degree = models.CharField(max_length=255)
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class Skill(TimestampedModel):
  type = models.CharField(max_length=64)
  name = models.CharField(max_length=100)
  profiency = models.IntegerField(choices=[(1,1),(2,2),(3,3),(4,4),(5,5)])