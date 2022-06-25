import graphene
from server.models import *
from .types import *
from .decorators import *

class CreateEmployment(graphene.Mutation):
  class Arguments:
    start_date = graphene.Date()
    end_date = graphene.Date(required=False)
    # en
    company_en = graphene.String()
    position_en = graphene.String()
    status_en = graphene.String()
    descriptions_en = graphene.List(graphene.String)
    examples_en = graphene.List(graphene.String)
    # ja
    company_ja = graphene.String()
    position_ja = graphene.String()
    status_ja = graphene.String()
    descriptions_ja = graphene.List(graphene.String)
    examples_ja = graphene.List(graphene.String)
    # foreign keys
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

class CreateEducation(graphene.Mutation):
  class Arguments:
    start_date = graphene.Date()
    end_date = graphene.Date(required=False)
    degree = graphene.String()
    # en
    school_en = graphene.String()
    department_en = graphene.String()
    faculty_en = graphene.String()
    awards_en = graphene.List(graphene.String)
    research_en = graphene.String(required=False)
    # ja
    school_ja = graphene.String()
    department_ja = graphene.String()
    faculty_ja = graphene.String()
    awards_ja = graphene.List(graphene.String)
    research_ja = graphene.String(required=False)
    # foreign keys
    person_id = graphene.Int()

  ok = graphene.Boolean()
  education = graphene.Field(EducationType)

  @authenticated_only
  def mutate(root, info, **kwargs):
    ok = graphene.Boolean()
    education = Education(**kwargs)
    education.save()
    return CreateEducation(ok=ok, education=education)

class EditEducation(CreateEducation):
  class Arguments(CreateEducation.Arguments):
    id = graphene.Int()

  ok = graphene.Boolean()
  education = graphene.Field(EducationType)

  @authenticated_only
  def mutate(root, info, id, **kwargs):
    education = Education(pk=id, **kwargs)
    education.save(update_fields=kwargs.keys())
    return EditEducation(ok=True, education=education)

class Mutation(graphene.ObjectType):
  create_employment = CreateEmployment.Field()
  edit_employment = EditEmployment.Field()
  create_education = CreateEducation.Field()
  edit_education = EditEducation.Field()
