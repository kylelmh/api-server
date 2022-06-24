import graphene
import server.schema

class Query(server.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)