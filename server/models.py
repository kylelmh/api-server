from django.contrib.auth.models import User
from django.db import models
from datetime import datetime
from django_jsonform.models.fields import ArrayField
# Create your models here.

class TimestampedModel(models.Model):
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  class Meta:
    abstract = True

class Person(TimestampedModel):
  first_name = models.CharField(max_length=255)
  name = models.CharField(max_length=255)
  date_of_birth = models.DateField(default=datetime.now)
  email = models.EmailField(max_length=255)
  phone = models.CharField(max_length=255)
  city = models.CharField(max_length=255)
  country = models.CharField(max_length=255)
  
  def __str__(self):
    return f'{self.name} - {self.city}, {self.country}'

class Employment(TimestampedModel):
  start_date = models.DateField(default=datetime.now)
  end_date = models.DateField(null=True, blank=True)
  # en
  company_en = models.CharField(max_length=255)
  position_en = models.CharField(max_length=255)
  status_en = models.CharField(max_length=255)
  descriptions_en = ArrayField(default=list, base_field=models.CharField(max_length=255))
  examples_en = ArrayField(default=list, base_field=models.CharField(max_length=255))
  # ja
  company_ja = models.CharField(max_length=255)
  position_ja = models.CharField(max_length=255)
  status_ja = models.CharField(max_length=255)
  descriptions_ja = ArrayField(default=list, base_field=models.CharField(max_length=255))
  examples_ja = ArrayField(default=list, base_field=models.CharField(max_length=255))
  # foreign keys
  person = models.ForeignKey(Person, on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.start_date} - {self.end_date}: {self.position_en} - {self.company_en}'

class SkillTag(TimestampedModel):
  name = models.CharField(max_length=255, primary_key=True, unique=True)
  employments = models.ManyToManyField(Employment, related_name='skill_tags', blank=True)
  def __str__(self):
    return self.name

class Education(TimestampedModel):
  start_date = models.DateField(default=datetime.now)
  end_date = models.DateField(default=datetime.now)
  degree = models.CharField(max_length=255)
  # en
  school_en = models.CharField(max_length=255)
  department_en = models.CharField(max_length=255)
  faculty_en = models.CharField(max_length=255)
  awards_en = ArrayField(default=list, null=True, base_field=models.CharField(max_length=255))
  research_en = models.CharField(max_length=255, null=True)
  # ja
  school_ja = models.CharField(max_length=255)
  department_ja = models.CharField(max_length=255)
  faculty_ja = models.CharField(max_length=255)
  awards_ja = ArrayField(default=list, null=True, base_field=models.CharField(max_length=255))
  research_ja = models.CharField(max_length=255, null=True)
  # foreign keys
  person = models.ForeignKey(Person, on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.start_date} - {self.end_date}: {self.school_en} - {self.degree}'
  
class Publication(TimestampedModel):
  citation = models.CharField(max_length=255)
  education = models.ForeignKey(Education, null=True, on_delete=models.DO_NOTHING)
  employment = models.ForeignKey(Employment, null=True, on_delete=models.DO_NOTHING)

class Skill(TimestampedModel):
  type = models.CharField(max_length=64)
  name = models.CharField(max_length=255)
  profiency = models.IntegerField(choices=[(1,1),(2,2),(3,3),(4,4),(5,5)])
  person = models.ForeignKey(Person, on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.person.name}: {self.type} - {self.name}({self.profiency})'