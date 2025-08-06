""" Prospect Model """

from masoniteorm.models import Model
from masoniteorm.relationships import has_one


class Prospect(Model):
    """Prospect Model"""

    @has_one('id', 'title_id')
    def title(self):
        from models.Title import Title
        return Title

    @has_one('id', 'nationality_id')
    def nationality(self):
        from models.Nationality import Nationality
        return Nationality
