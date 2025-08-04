"""DepartmentsTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from models.Department import Department


class DepartmentsTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        
        Department.bulk_create([
            {
                "id": '00000000-0000-2000-8000-a10000000000',
                "name": "Sales & Marketing",
            },
            {
                "id": '00000000-0000-2000-8000-a10000000001',
                "name": "Technical/Underwriting",
            },
            {
                "id": '00000000-0000-2000-8000-a10000000002',
                "name": "Claims Management",
            },
            {
                "id": '00000000-0000-2000-8000-a10000000003',
                "name": "Administration",
            },
            {
                "id": '00000000-0000-2000-8000-a10000000004',
                "name": "Customer Service",
            },
        ])

    # Sales & Marketing
    # Technical/Underwriting
    # Claims Management
    # Finance
    # Administration
    # Customer Service

