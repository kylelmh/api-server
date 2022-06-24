import graphene
import server.schema

class Query(server.schema.Query, graphene.ObjectType):
    pass

class Mutation(server.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)