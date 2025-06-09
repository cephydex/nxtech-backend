""" BizIntroducer Model """

from masoniteorm.models import Model
from masoniteorm.relationships import has_one


class BizIntroducer(Model):
    """BizIntroducer Model"""

    @has_one('id', 'title_id')
    def title(self):
        from models.Title import Title
        return Title
