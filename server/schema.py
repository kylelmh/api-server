import graphene
from graphene.types.generic import GenericScalar # Solution
from graphene_django.types import DjangoObjectType
from .models import *


class PersonType(DjangoObjectType):
  class Meta:
    model = Person

class EmploymentType(DjangoObjectType):
  class Meta:
    model = Employment

class EducationType(DjangoObjectType):
  class Meta:
    model = Education

class Query(object):
  lee = graphene.Field(PersonType)

  def resolve_lee(self, info):
    return Person.objects.filter(name='Lee').first()
