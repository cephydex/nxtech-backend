""" Prospect Model """

from masoniteorm.models import Model
from masoniteorm.relationships import has_one, has_many


class Prospect(Model):
    """Prospect Model"""
    # __selects__ = ["username", "administrator as is_admin"]

    @has_one('id', 'title_id')
    def title(self):
        from models.Title import Title
        return Title

    @has_one('id', 'nationality_id')
    def nationality(self):
        from models.Nationality import Nationality
        return Nationality
    
    # @has_many("prospect_id", "id")
    @has_many("id", "prospect_id")
    def stages(self):
        from models.ProspectStage import ProspectStage
        return ProspectStage
