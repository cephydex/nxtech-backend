""" Policy Model """

from masoniteorm.models import Model
from masoniteorm.relationships import has_one


class Policy(Model):
    """Policy Model"""

    @has_one('id', 'quote_id')
    def quote(self):
        from models.Quote import Quote
        return Quote
