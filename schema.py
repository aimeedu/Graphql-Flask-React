import graphene
import json
from datetime import datetime


class User(graphene.ObjectType):
    id = graphene.ID()
    username = graphene.String()
    lastLogin = graphene.DateTime(required=False)


class Query(graphene.ObjectType):
    users = graphene.List(User, first=graphene.Int())

    def resolve_users(self, info, first):
        return [
            User(username='Aimee', lastLogin=datetime.now()),
            User(username='Akhil', lastLogin=datetime.now()),
            User(username='Yaniv', lastLogin=datetime.now()),
        ][:first]


# inherite class Mutation, like calling super
class CreateUser(graphene.Mutation):
    class Arguments:
        username = graphene.String()
    user = graphene.Field(User)

    def mutate(self, info, username):
        user = User(username=username)
        return CreateUser(user=user)


class Mutations(graphene.ObjectType):
    createUser = CreateUser.Field()


schema = graphene.Schema(query=Query, mutation=Mutations, auto_camelcase=False)

result = schema.execute(
    '''
    {
        # users(first: 2) {
        #     username
        #     lastLogin
        # }

        mutation createUser {
            createUser(username: "Bob") {
                user {
                    username
                }
            }
        }

    }
    '''
)

# items = dict(result.data.items())

# print(json.dumps(items, indent=4))
print(result.data)
