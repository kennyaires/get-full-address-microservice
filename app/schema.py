import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from app.models.address import Address as AddressModel


class Address(SQLAlchemyObjectType):
    class Meta:
        model = AddressModel
        interfaces = (relay.Node, )


class SearchResult(graphene.Union):
    class Meta:
        types = (Address,)


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    search = graphene.List(SearchResult, q=graphene.String())  # List field for search results

    all_addresses = SQLAlchemyConnectionField(Address.connection)

    def resolve_search(self, info, **args):
        q = args.get("q")  # Search query

        # Get queries
        address_query = Address.get_query(info)

        # Query Addresses
        addresses = address_query.filter((AddressModel.postal_code.contains(q)) | 
                                        (AddressModel.address.contains(q))).all()

        return addresses

schema = graphene.Schema(query=Query, types=[Address])
