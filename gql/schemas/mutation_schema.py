from gql.controllers import Mutations
from typing import List
from gql.schemas import data_schema as schemas
import strawberry


@strawberry.type
class Mutation:

    add_single_title:schemas.Title = strawberry.field(resolver=Mutations.add_title)

