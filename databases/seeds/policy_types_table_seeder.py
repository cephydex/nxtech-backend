"""PolicyTypesTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from models.PolicyType import PolicyType

class PolicyTypesTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        
        PolicyType.bulk_create([
            {
                "id": "00000000-0000-5000-8000-a10000000000", 
                "cat_id": "00000000-0000-3000-8000-a10000000000", 
                "name": "Comprehensive",
                "description": "Comprehensive",
                "commission": 16.50,
            },
            {
                "id": "00000000-0000-5000-8000-a10000000001", 
                "cat_id": "00000000-0000-3000-8000-a10000000000", 
                "name": "Third Party",
                "description": "Third Party",
                "commission": 10.00,
            },
            {
                "id": "00000000-0000-5000-8000-a10000000002", 
                "cat_id": "00000000-0000-3000-8000-a10000000000", 
                "name": "Third Party Fire & Theft",
                "description": "Third Party Fire & Theft",
                "commission": 10.00,
            },
        ])

        PolicyType.bulk_create([
            {
                "id": "00000000-0000-5000-8000-a10000000003", 
                "cat_id": "00000000-0000-3000-8000-a10000000001", 
                "name": "Assets All Risks",
                "description": "Assets All Risks",
                "commission": 21.00,
            },
            {
                "id": "00000000-0000-5000-8000-a10000000004", 
                "cat_id": "00000000-0000-3000-8000-a10000000003", 
                "name": "Marine Cargo",
                "description": "Marine Cargo",
                "commission": 15.00,
            },
            {
                "id": "00000000-0000-5000-8000-a10000000005", 
                "cat_id": "00000000-0000-3000-8000-a10000000003", 
                "name": "Marine Hull",
                "description": "Marine Hull",
                "commission": 15.00,
            },
            
        ])

        pass

    
    # Assets All Risks	21.00%
    # Fire & Allied Perils	21.00%
    # Consequential Loss	21.00%
    # Public Liability	20.00%
    # Public and Product Liability	20.00%
    # General Liability	20.00%
    # Employers’ Liability	20.00%
    # Professional Indemnity	20.00%
    # Product Liability	20.00%
    # Marine Cargo	15.00%
    # Marine Hull	15.00%
    # Goods in Transit	20.00%
    # Contractors’ All Risks (CAR)	20.00%
    # Erection All Risks (EAR)	20.00%
    # Machinery Breakdown	20.00%
    # Plant & Machinery	20.00%
    # Electronic Equipment Insurance (EEI)	20.00%
    # Stock Deterioration	20.00%
    # Money Insurance	20.00%
    # Fidelity Guarantee	20.00%
    # Group Personal Accident (GPA)	20.00%
    # Individual Personal Accident	20.00%
    # Travel Insurance	10.00%
    # Bonds – Bid Bond	20.00%
    # Bonds – Performance Bond	20.00%
    # Bonds – Advance Payment Bond	20.00%
    # Bonds – Retention Bond	20.00%
    # Bonds – Customs Warehouse Bonds	20.00%
    # Bonds – Customs Removal Bonds	20.00%
    # Bonds – Customs Re/Exportation Bonds	20.00%
    # Bonds – Customs Temporary Importation Bonds	20.00%
    # Credit Guarantee / Trade Credit Insurance	20.00%
    # Agriculture – Crop Insurance	10.00%
    # Agriculture – Livestock Insurance	10.00%
    # Property Terrorism & Sabotage	20.00%
    # Goods in Transit	20.00%
    # Fidelity Guarantee	20.00%
    # Group Life Assurance	20.00%
    # Individual Term Life	20.00%
    # Credit Life 	20.00%
    # Funeral Insurance 	20.00%
    # Health Insurance 	10.00%
    # International Health Plans	10.00%
    # Money Insurance	20.00%
    # Mobile Phone Insurance	20.00%
    # Other 	

