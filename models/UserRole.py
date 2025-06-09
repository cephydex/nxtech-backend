""" Role Model """

from masoniteorm.models import Model


class UserRole(Model):
    """Role Model"""

    pass

    def as_dict(self):
        return {
            'id': str(self.id),
            'name': self.name,
            'description': self.description,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }
