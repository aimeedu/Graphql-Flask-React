from flask import Flask
from graphene import ObjectType, String, Schema, Int
from flask_graphql import GraphQLView

app = Flask(__name__)


class Query(ObjectType):
    hello = String(name=String(default_value="Aimee"),
                   age=Int(default_value=12))
    googbye = String()

    def resolve_hello(self, info, name, age):
        return f'Hello {name} {age}!'

    def resolve_goodbye(self, info):
        return 'See ya!'

# For each Field in our Schema, we write a Resolver method to fetch data requested by a client’s Query using the current context and Arguments.


schema = Schema(query=Query)


app.add_url_rule(
    '/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

# Optional, for adding batch query support (used in Apollo-Client)
# app.add_url_rule('/graphql/batch',
#                  view_func=GraphQLView.as_view('graphql', schema=schema, batch=True))

app.run(port=4901)

# query_st = '{ hello }'
# result = schema.execute(query_st)
# print(result.data)
# print(result.data['hello'])

# with_args = '{ hello(name: "Lucy", age: 3)}'
# result = schema.execute(with_args)
# print(result.data['hello'])


# Schema

# Query fetches data
# Mutation to changes data and retrieve the changes
# Subscription to sends changes to clients in real time
