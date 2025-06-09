""" Institution Model """

from masoniteorm.models import Model


class Institution(Model):
    """Institution Model"""

    pass


    def as_dict(self):
        return {
            'id': str(self.id),
            'name': self.name,
            'description': self.description,
            'phone_no': self.phone_no,
            'address': self.address,
            'email': self.email,

            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }
