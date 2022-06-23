import graphene
from graphene.types.generic import GenericScalar # Solution
from graphene_django.types import DjangoObjectType
from .models import *

class EmploymentType(DjangoObjectType):
  class Meta:
    model = Employment

class Query(object):
  all_employments = graphene.List(EmploymentType)

  def resolve_all_employments(self, info, **kwargs):
    return Employment.objects.all()

class CreateEmployment(graphene.Mutation):
    employment= graphene.Field(EmploymentType)

    def mutate(self, info, lat, lon, name):
        loc = Employment(lat=lat, lon=lon, name=name)
        loc.save()
        return CreateEmployment(location=loc)

class Mutation(graphene.ObjectType):
  create_employment = CreateEmployment.Field()