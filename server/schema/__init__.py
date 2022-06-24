from .query import Query
from .mutations import Mutation

globals()['Query'] = Query
globals()['Mutation'] = Mutation