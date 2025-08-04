"""PolicyCategoriesTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from models.PolicyCategory import PolicyCategory


class PolicyCategoriesTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""

        PolicyCategory.bulk_create([
            {"id": "00000000-0000-3000-8000-a10000000000", "name": "Motor Insurance"},
            {"id": "00000000-0000-3000-8000-a10000000001", "name": "Fire & Property Damage"},
            {"id": "00000000-0000-3000-8000-a10000000002", "name": "Liability Insurance"},
            {"id": "00000000-0000-3000-8000-a10000000003", "name": "Marine & Aviation Insurance"},
            {"id": "00000000-0000-3000-8000-a10000000004", "name": "Inland Transit"},
            {"id": "00000000-0000-3000-8000-a10000000005", "name": "Engineering Insurance"},
            {"id": "00000000-0000-3000-8000-a10000000006", "name": "Health / Medical Insurance/Travel Insurance"},
            {"id": "00000000-0000-3000-8000-a10000000007", "name": "Bonds, Guarantees & Credit Insurance"},
            {"id": "00000000-0000-3000-8000-a10000000008", "name": "Agriculture Insurance"},
            {"id": "00000000-0000-3000-8000-a10000000009", "name": "Accident Insurance"},
            {"id": "00000000-0000-3000-8000-a10000000010", "name": "Other"},
        ])
