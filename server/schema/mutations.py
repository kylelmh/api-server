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
    skill_tags = graphene.List(graphene.String)

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

class CreatePerson(graphene.Mutation):
  class Arguments:
    first_name = graphene.String()
    name = graphene.String()
    date_of_birth = graphene.Date()
    email = graphene.String()
    phone = graphene.String()
    city = graphene.String()
    country =  graphene.String()

  ok = graphene.Boolean()
  person = graphene.Field(PersonType)

  @authenticated_only
  def mutate(root, info, **kwargs):
    ok = graphene.Boolean()
    person = Person(**kwargs)
    person.save()
    return CreatePerson(ok=ok, person=person)

class EditPerson(CreatePerson):
  class Arguments(CreatePerson.Arguments):
    id = graphene.Int()
  
  ok = graphene.Boolean()
  person = graphene.Field(PersonType)

  @authenticated_only
  def mutate(root, info, id, **kwargs):
    person = Person(pk=id, **kwargs)
    person.save(update_fields=kwargs.keys())
    return EditPerson(ok=True, person=person)

class CreateSkill(graphene.Mutation):
  class Arguments:
    type = graphene.String()
    name = graphene.String()
    proficieny = graphene.Int()
    # foreign keys
    person_id = graphene.Int()

  ok = graphene.Boolean()
  skill = graphene.Field(SkillType)

  def mutate(root, info, **kwargs):
    ok = graphene.Boolean()
    skill = Skill(**kwargs)
    skill.save()
    return CreateSkill(ok=ok, skill=skill)

class EditSkill(CreateSkill):
  class Arguments(CreateSkill.Arguments):
    id = graphene.Int()
  
  ok = graphene.Boolean()
  skill = graphene.Field(SkillType)

  def mutate(root, info, id, **kwargs):
    skill = Skill(pk=id, **kwargs)
    skill.save(update_fields=kwargs.keys())
    return EditSkill(ok=True, skill=skill)

class CreateSkillTag(graphene.Mutation):
  class Arguments():
    name = graphene.String()
    employments = graphene.List(graphene.Int)
  
  ok = graphene.Boolean()
  skill_tag = graphene.Field(SkillTagType)

  def mutate(root, info, **kwargs):
    skill_tag = SkillTag(**kwargs)
    skill_tag.save()
    return CreateSkillTag(ok=True, skill_tag=skill_tag)

class EditSkillTag(CreateSkillTag):
  ok = graphene.Boolean()
  skill_tag = graphene.Field(SkillTagType)

  def mutate(root, info, **kwargs):
    skill_tag = SkillTag(**kwargs)
    skill_tag.save(update_fields=kwargs.keys())
    return EditSkillTag(ok=True, skill_tag=skill_tag)

class Mutation(graphene.ObjectType):
  create_employment = CreateEmployment.Field()
  edit_employment = EditEmployment.Field()
  create_education = CreateEducation.Field()
  edit_education = EditEducation.Field()
  create_person = CreatePerson.Field()
  edit_person = EditPerson.Field()
  create_skill = CreateSkill.Field()
  edit_skill = EditSkill.Field()
  create_skill_tag = CreateSkillTag.Field()
  edit_skill_tag = EditSkillTag.Field()

