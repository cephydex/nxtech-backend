"""ProfessionalGroupsTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from models.ProfessionalGroup import ProfessionalGroup


class ProfessionalGroupsTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        
        ProfessionalGroup.bulk_create([
            # {
            #     "id": "ecf554fc-fc36-4970-a089-e7745376dbd0",
            #     "name": "Account Administration",
            # },
            {
                "id": "ecf554fc-fc36-4970-a000-e70000000001",
                "name": "Logistics",
            },
        ])
