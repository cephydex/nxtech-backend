""" Project Model """

from masoniteorm.models import Model
from masoniteorm.relationships import has_many, has_one


class Project(Model):
    """Project Model"""

    @has_many("id", "project_id")
    def stages(self):
        from models.ProspectionStage import ProspectionStage
        return ProspectionStage

    @has_one("id", "prospect_id")
    def prospect(self):
        from models.Prospect import Prospect
        return Prospect

    @has_one("id", "policy_type_id")
    def product(self):
        from models.PolicyCategory import PolicyCategory
        return PolicyCategory
