""" User Model """

from masoniteorm.models import Model
from masoniteorm.scopes import scope
from masoniteorm.relationships import has_one


class User(Model):
    """User Model"""

    @has_one('id', 'role_id')
    def role(self):
        from models.UserRole import UserRole
        return UserRole

    def as_dict(self):
        return {
            'id': str(self.id),
            'username': self.username,
            'email': self.email,
            # 'phone': self.phone,
            'password': self.password,
            'active_status': self.active_status,
            'role_id': self.role_id,
        }

    @scope
    def by_email(self, query, email):
        return query.where('email', '=', email)


    @scope
    def by_username(self, query, username):
        return query.where('username', '=', username)
