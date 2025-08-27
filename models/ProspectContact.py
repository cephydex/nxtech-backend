""" ProspectContact Model """

from masoniteorm.models import Model
from masoniteorm.relationships import has_one


class ProspectContact(Model):
    """ProspectContact Model"""

    @has_one('id', 'prospect_id')
    def prospect(self):
        from models.Prospect import Prospect
        return Prospect
