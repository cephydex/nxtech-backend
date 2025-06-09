"""MusigaTitlesTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from models.Title import Title


class TitlesTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        # pass
        
        Title.bulk_create([
            {
                "id": '00000000-0000-4000-8000-a10000000000',
                "name": "Mr",
                # "is_active": True,
            },
            {
                "id": '00000000-0000-4000-8000-a20000000000',
                "name": "Mrs",
                # "is_active": True,
            },
            {
                "id": '00000000-0000-4000-8000-a30000000000',
                "name": "Miss",
                # "is_active": True,
            },
            {
                "id": '00000000-0000-4000-8000-a40000000000',
                "name": "Dr",
                # "is_active": True,
            },
            {
                "id": '00000000-0000-4000-8000-a50000000000',
                "name": "Prof",
                # "is_active": True,
            },
        ])
