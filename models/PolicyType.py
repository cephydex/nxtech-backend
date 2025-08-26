""" PolicyType Model """

from masoniteorm.models import Model
from masoniteorm.relationships import has_one


class PolicyType(Model):
    """PolicyType Model"""

    @has_one("id", "cat_id")
    def policy_category(self):
        from models.PolicyCategory import PolicyCategory
        return PolicyCategory
