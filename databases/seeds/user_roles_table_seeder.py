"""RoleTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from models.UserRole import UserRole


class UserRolesTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""

        UserRole.bulk_create([
                {
                    "id": "71f094df-7fcb-4f91-b305-235b412a7af1",
                    "name": "super-admin",
                    "description": "super-admin",
                },
                {
                    "id": "71f094df-7fcb-4f91-b305-235b412a7af2",
                    "name": "admin",
                    "description": "admin",
                },
                {
                    "id": "71f094df-7fcb-4f91-b305-235b412a7afa",
                    "name": "fin-admin",
                    "description": "finance/admin",
                },
                {
                    "id": "71f094df-7fcb-4f91-b305-235b412a7afb",
                    "name": "broking-officer",
                    "description": "broking-officer",
                },
                {
                    "id": "71f094df-7fcb-4f91-b305-235b412a7ae1",
                    "name": "claims-officer",
                    "description": "claims-officer",
                },
                {
                    "id": "71f094df-7fcb-4f91-b305-235b412a7ae2",
                    "name": "biz-introducer",
                    "description": "biz-introducer",
                },
            ])
        
# Admin (full access) 
# Management 
# Broking Officers 
# Claims Officers 
# Finance/Admin (premium & commission sections only) 
# Business Introducers Introducers (restricted view of their own records – optional) 

