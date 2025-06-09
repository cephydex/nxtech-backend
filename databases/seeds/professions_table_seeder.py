"""ProfessionsTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from models.Profession import Profession


class ProfessionsTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        
        Profession.bulk_create([
            {
                "id": "ecf554fc-fc36-4970-a089-000000000001",
                "name": "Transportation",
                "code": "003",
                "group_id": 'ecf554fc-fc36-4970-a089-e7745376dbd0'
            },
            {
                "id": "ecf554fc-fc36-4970-a089-000000000001",
                "name": "Logistics",
                "code": "003",
                "group_id": 'ecf554fc-fc36-4970-a089-e7745376dbd0'
            },
        ])
