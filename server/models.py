from django.db import models

# Create your models here.

class TimestampedModel(models.Model):
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  class Meta:
    abstract = True

class Employment(TimestampedModel):
  start_date = models.DateField
  end_date = models.DateField
  position = models.JSONField
  status = models.CharField(max_length=255)
  company = models.JSONField
  description = models.JSONField

class Education(TimestampedModel):
  start_date = models.DateField
  end_date = models.DateField
  school = models.JSONField
  faculty = models.JSONField
  department = models.JSONField
  degree = models.CharField(max_length=255)
  description = models.JSONField

class Skill(TimestampedModel):
  type = models.CharField(max_length=64)
  name = models.CharField(max_length=100)
  profiency = models.IntegerField(choices=[(1,1),(2,2),(3,3),(4,4),(5,5)])