""" ProspectionStage Model """

from masoniteorm.models import Model
from masoniteorm.relationships import has_one


class ProspectionStage(Model):
    """ProspectionStage Model"""

    @has_one('id', 'client_id')
    def client(self):
        from models.Client import Client
        return Client

    @has_one('id', 'user_id')
    def user(self):
        from models.User import User
        return User
