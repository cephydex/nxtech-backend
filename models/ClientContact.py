""" ClientContact Model """

from masoniteorm.models import Model
from masoniteorm.relationships import has_one


class ClientContact(Model):
    """ClientContact Model"""

    __table__ = "client_contacts"

    @has_one('id', 'client_id')
    def client(self):
        from models.Client import Client
        return Client

    pass
