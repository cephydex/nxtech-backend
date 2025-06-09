""" Profession Model """

from masoniteorm.models import Model
from masoniteorm.relationships import has_one


class Profession(Model):
    """Profession Model"""

    @has_one('id', 'group_id')
    def group(self):
        from models.ProfessionalGroup import ProfessionalGroup
        return ProfessionalGroup
