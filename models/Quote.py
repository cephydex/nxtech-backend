""" Quote Model """

from masoniteorm.models import Model
from masoniteorm.relationships import has_one, has_many


class Quote(Model):
    """Quote Model"""

    @has_one('id', 'prospect_id')
    def prospect(self):
        from models.Prospect import Prospect
        return Prospect

    @has_many('id', 'quote_id')
    def quote_extras(self):
        from models.QuoteExtra import QuoteExtra
        return QuoteExtra
