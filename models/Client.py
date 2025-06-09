""" Client Model """

from masoniteorm.models import Model
from masoniteorm.relationships import has_one


class Client(Model):
    """Client Model"""

    @has_one('id', 'title_id')
    def title(self):
        from models.Title import Title
        return Title

    @has_one('id', 'nationality_id')
    def title(self):
        from models.Nationality import Nationality
        return Nationality

    @has_one('id', 'profession_id')
    def title(self):
        from models.Profession import Profession
        return Profession

    # @has_one('id', 'profession_id')
    # def title(self):
    #     from models.Title import Title
    #     return Title
