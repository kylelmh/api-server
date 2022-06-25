import graphene
from server.models import *
from .types import *
from .decorators import *

class CreateEmployment(graphene.Mutation):
  class Arguments:
    start_date = graphene.Date()
    end_date = graphene.Date(required=False)
    company_en = graphene.String()
    position_en = graphene.String()
    status_en = graphene.String()
    descriptions_en = graphene.List(graphene.String)
    examples_en = graphene.List(graphene.String)
    company_ja = graphene.String()
    position_ja = graphene.String()
    status_ja = graphene.String()
    descriptions_ja = graphene.List(graphene.String)
    examples_ja = graphene.List(graphene.String)
    person_id = graphene.Int()

  ok = graphene.Boolean()
  employment = graphene.Field(EmploymentType)

  @authenticated_only
  def mutate(root, info, **kwargs):
    ok = graphene.Boolean()
    employment = Employment(**kwargs)
    employment.save()
    return CreateEmployment(ok=ok, employment=employment)

class EditEmployment(CreateEmployment):
  class Arguments(CreateEmployment.Arguments):
    id = graphene.Int()

  @authenticated_only
  def mutate(root, info, id, **kwargs):
    employment = Employment(pk=id, **kwargs)
    employment.save(update_fields=kwargs.keys())
    return EditEmployment(ok=True, employment=employment)

class Mutation(graphene.ObjectType):
  create_employment = CreateEmployment.Field()
  edit_employment = EditEmployment.Field()
