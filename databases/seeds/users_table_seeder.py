"""UsersTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from models.User import User
from utils.cjwt import get_password_hash


class UsersTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        
        User.bulk_create([
            {
                'id': '20000000-0000-4001-0000-010000000000',
                'email': 'user1@mail.com',
                'username': 'user1',
                'password': get_password_hash('g3nUs3r1'),
                "active_status": 'active',
                "role_id": '71f094df-7fcb-4f91-b305-235b412a7af1',
            },
            {
                'id': '20000000-0000-4001-0000-010000000001',
                'email': 'user2@mail.com',
                'username': 'user2',
                'password': get_password_hash('g3nUs3r2'),
                "active_status": 'pending',
                "role_id": '71f094df-7fcb-4f91-b305-235b412a7af2',
            },
            {
                'id': '20000000-0000-4001-0000-010000000002',
                'email': 'userb@mail.com',
                'username': 'userb',
                'password': get_password_hash('g3nUs3rb'),
                "active_status": 'pending',
                "role_id": '71f094df-7fcb-4f91-b305-235b412a7afb',
            },
        ])
        
        pass
    
        # table.uuid("id").primary()
        # table.string("email").unique()
        # table.string("username").unique()
        # table.string("password")
        # table.enum("active_status", ['pending', 'active', 'disabled']).default('active')
        
        # table.uuid("role_id"
