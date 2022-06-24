import graphene
from .types import *
from server.models import *

class Query(object):
  lee = graphene.Field(PersonType)

  def resolve_lee(self, info):
    return Person.objects.filter(name='Lee').first()