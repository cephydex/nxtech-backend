"""ProfessionsTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from models.Profession import Profession


class ProfessionsTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        
        Profession.bulk_create([
            {
                "id": "ecf554fc-fc36-4970-a089-000000000001",
                "name": "Farmer",
                "code": "003",
                "group_id": 'ecf554fc-fc36-4970-a000-e70000000001'
            },
            {
                "id": "ecf554fc-fc36-4970-a089-000000000002",
                "name": "Extension officer",
                "code": "004",
                "group_id": 'ecf554fc-fc36-4970-a000-e70000000001'
            },
            {
                "id": "ecf554fc-fc36-4970-a089-000000000003",
                "name": "Banker",
                "code": "005",
                "group_id": 'ecf554fc-fc36-4970-a000-e70000000002'
            },
            {
                "id": "ecf554fc-fc36-4970-a089-000000000004",
                "name": "Cashier",
                "code": "006",
                "group_id": 'ecf554fc-fc36-4970-a000-e70000000002'
            },
            {
                "id": "ecf554fc-fc36-4970-a089-000000000005",
                "name": "Bank Support Staff",
                "code": "007",
                "group_id": 'ecf554fc-fc36-4970-a000-e70000000002'
            },
            {
                "id": "ecf554fc-fc36-4970-a089-000000000006",
                "name": "Constructor",
                "code": "008",
                "group_id": 'ecf554fc-fc36-4970-a000-e70000000003'
            },
            {
                "id": "ecf554fc-fc36-4970-a089-000000000007",
                "name": "Electrician",
                "code": "009",
                "group_id": 'ecf554fc-fc36-4970-a000-e70000000003'
            },
        ])
