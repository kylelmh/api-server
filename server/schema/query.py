import graphene
from .types import *
from server.models import *

class Query(object):
  lee = graphene.Field(PersonType)
  employments_of = graphene.List(EmploymentType, name=graphene.String())
  educations_of = graphene.List(EducationType, name=graphene.String())
  cv_of = graphene.Field(PersonType, name=graphene.String()) 

  def resolve_lee(self, info):
    return Person.objects.filter(name='Lee').first()

  def resolve_employments_of(self, info, name):
    return Employment.objects.filter(person__name=name)

  def resolve_educations_of(self, info, name):
    return Education.objects.filter(person__name=name)

  def resolve_cv_of(self, info, name):
    return Person.objects.filter(name=name).first()