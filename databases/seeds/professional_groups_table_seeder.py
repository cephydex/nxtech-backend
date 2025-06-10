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
                "name": "Agriculture & Agribusiness",
            },
            {
                "id": "ecf554fc-fc36-4970-a000-e70000000002",
                "name": "Banking, Finance & Insurance",
            },
            {
                "id": "ecf554fc-fc36-4970-a000-e70000000003",
                "name": "Construction & Real Estate",
            },
            {
                "id": "ecf554fc-fc36-4970-a000-e70000000004",
                "name": "Education & Training",
            },
            {
                "id": "ecf554fc-fc36-4970-a000-e70000000005",
                "name": "Energy & Utilities",
            },
            {
                "id": "ecf554fc-fc36-4970-a000-e70000000006",
                "name": "Manufacturing & Industry",
            },
            {
                "id": "ecf554fc-fc36-4970-a000-e70000000007",
                "name": "Healthcare & Medical Services",
            },
            {
                "id": "ecf554fc-fc36-4970-a000-e70000000008",
                "name": "Hospitality & Tourism",
            },
            {
                "id": "ecf554fc-fc36-4970-a000-e70000000009",
                "name": "Information & Communication Technology (ICT)",
            },
            {
                "id": "ecf554fc-fc36-4970-a000-e70000000010",
                "name": "Legal & Professional Services",
            },
            {
                "id": "ecf554fc-fc36-4970-a000-e70000000011",
                "name": "Logistics & Transportation",
            },
            {
                "id": "ecf554fc-fc36-4970-a000-e70000000012",
                "name": "Media & Creative Arts",
            },
            {
                "id": "ecf554fc-fc36-4970-a000-e70000000013",
                "name": "Mining & Natural Resources",
            },
            {
                "id": "ecf554fc-fc36-4970-a000-e70000000014",
                "name": "NGO & Development Sector",
            },
            {
                "id": "ecf554fc-fc36-4970-a000-e70000000015",
                "name": "Public Sector / Government Services",
            },
            {
                "id": "ecf554fc-fc36-4970-a000-e70000000016",
                "name": "Retail & Wholesale Trade",
            },
            {
                "id": "ecf554fc-fc36-4970-a000-e70000000017",
                "name": "Import & Export",
            },
            {
                "id": "ecf554fc-fc36-4970-a000-e70000000018",
                "name": "Telecommunications",
            },
            {
                "id": "ecf554fc-fc36-4970-a000-e70000000019",
                "name": "Individual Professionals / Freelancers",
            },
            {
                "id": "ecf554fc-fc36-4970-a000-e70000000020",
                "name": "Entrepreneaur",
            },
            {
                "id": "ecf554fc-fc36-4970-a000-e70000000021",
                "name": "Businessman/Business Woman",
            },
            {
                "id": "ecf554fc-fc36-4970-a000-e70000000022",
                "name": "Students",
            },
            {
                "id": "ecf554fc-fc36-4970-a000-e70000000023",
                "name": "Retired Persons",
            },
            {
                "id": "ecf554fc-fc36-4970-a000-e70000000024",
                "name": "Unemployed / Informal Sector",
            },
            {
                "id": "ecf554fc-fc36-4970-a000-e70000000025",
                "name": "Religious & Faith-Based Organizations",
            },
            {
                "id": "ecf554fc-fc36-4970-a000-e70000000026",
                "name": "Others (Specify)",
            },
# 1.	Agriculture & Agribusiness
# 2.	Banking, Finance & Insurance
# 3.	Construction & Real Estate
# 4.	Education & Training
# 5.	Energy & Utilities
# 6.	Manufacturing & Industry
# 7.	Healthcare & Medical Services
# 8.	Hospitality & Tourism
# 9.	Information & Communication Technology (ICT)
# 10.	Legal & Professional Services
# 11.	Logistics & Transportation
# 12.	Media & Creative Arts
# 13.	Mining & Natural Resources
# 14.	NGO & Development Sector
# 15.	Public Sector / Government Services
# 16.	Retail & Wholesale Trade
# 17.	Import & Export
# 18.	Telecommunications
# 19.	Individual Professionals / Freelancers
# 20.	Entrepreneaur
# 21.	Businessman/Business Woman
# 22.	Students
# 23.	Retired Persons
# 24.	Unemployed / Informal Sector
# 25.	Religious & Faith-Based Organizations
# 26.	Others (Specify)

        ])
