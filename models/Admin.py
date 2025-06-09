""" Admin Model """

from masoniteorm.models import Model
from masoniteorm.scopes import scope
from masoniteorm.relationships import has_one


class Admin(Model):
    """Admin Model"""
    __primary_key__ = "id"
    # __fillable__ = ["email", "active", "password"]


    def __repr__(self):
        return '(id=%s, first_name=%s, last_name=%s, other_names=%s, sex=%s, phone=%s)' % \
                (self.id, self.first_name, self.last_name, self.other_names, self.sex, self.phone)


    @has_one('id', 'role_id')
    def role(self):
        from models.UserRole import Role
        return Role


    @scope
    def by_email(self, query, email):
        return query.where('email', '=', email)


    @scope
    def by_phone(self, query, phone):
        return query.where('phone', '=', phone)
    

    def as_dict(self):
        return {
            'id': str(self.id),
            'first_name': self.first_name,
            'last_name': self.last_name,
            'other_names': self.other_names,
            'sex': self.sex,
            'email': self.email,
            'phone': self.phone,
            'password': self.password,
            'active_status': self.active_status,
            'role_id': self.role_id,
            'inst': self.inst,

            # 'created_at': str(self.created_at),
            # 'updated_at': str(self.updated_at),
        }
    
# users = User.find([1,2,3])
# for users in users:
#   user.name #== 'Joe'
