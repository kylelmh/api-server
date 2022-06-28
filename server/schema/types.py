from graphene_django.types import DjangoObjectType
from server.models import *


class PersonType(DjangoObjectType):
  class Meta:
    model = Person

class EmploymentType(DjangoObjectType):
  class Meta:
    model = Employment

class EducationType(DjangoObjectType):
  class Meta:
    model = Education

class SkillType(DjangoObjectType):
  class Meta:
    model = Skill

class SkillTagType(DjangoObjectType):
  class Meta:
    model = SkillTag