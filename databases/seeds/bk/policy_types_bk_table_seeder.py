"""PolicyTypesTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from models.PolicyType import PolicyType

class PolicyTypesTableSeeder(Seeder):

    def getInitId(self, uuid_str:str = None):
        # import re
        chk = uuid_str if uuid_str else '00000000-0000-4001-0001-c00100000000'
        last_id = chk.rsplit("-", 1)[1]
        int_part = int(''.join(filter(str.isdigit, last_id)))
        
        return int_part

    def getInitId2(self, uuid_str:str = None):
        last_id = uuid_str if uuid_str else '00000000-0000-4001-0001-c00100000000'
        last_id = last_id.rsplit("-", 1)[1]
        int_part = int(''.join([char for char in last_id if char.isdigit()]))
        # nums = re.findall(r'\d+', last_id)
        return int_part

    def getInitId3(self, uuid_str:str = None):
        import re
        last_id = uuid_str if uuid_str else '00000000-0000-4001-0001-c00100000000'
        last_id = last_id.rsplit("-", 1)[1]
        int_part = re.findall(r'\d+', last_id)
        return int_part

    from typing import List
    def get_db_entry(self, options:dict, product_cat_id:str, last_num:int) -> dict:
        db_data = []
        for opt in options:
            db_data.append({
                "id": "00000000-0000-5000-8000-a"+str(last_num), 
                "cat_id": product_cat_id,
                "name": opt,
                "description": opt,
                "commission": options.get(opt),
            })
            print(f'Num: {last_num}', opt, options.get(opt))
            last_num = (last_num + 1)
        
        return {'data': db_data, 'last_num': last_num}

    def run(self):
        """Run the database seeds."""

        print('LAST ID', self.getInitId("00000000-0000-5000-8000-a10000000000"))
        # print('LAST ID 2', self.getInitId2("00000000-0000-5000-8000-a10000000003"))
        # print('LAST ID 3', self.getInitId3("00000000-0000-5000-8000-a10000000003"))
        print('\n')
        last_num:int = self.getInitId("00000000-0000-5000-8000-a10000000000")
        # PolicyType.bulk_create([
        #     {
        #         "id": "00000000-0000-5000-8000-a10000000000", 
        #         "cat_id": "00000000-0000-3000-8000-a10000000000", 
        #         "name": "Comprehensive",
        #         "description": "Comprehensive",
        #         "commission": 16.50,
        #     },
        #     {
        #         "id": "00000000-0000-5000-8000-a10000000001", 
        #         "cat_id": "00000000-0000-3000-8000-a10000000000", 
        #         "name": "Third Party",
        #         "description": "Third Party",
        #         "commission": 10.00,
        #     },
        #     {
        #         "id": "00000000-0000-5000-8000-a10000000002", 
        #         "cat_id": "00000000-0000-3000-8000-a10000000000", 
        #         "name": "Third Party Fire & Theft",
        #         "description": "Third Party Fire & Theft",
        #         "commission": 10.00,
        #     },
        #     {
        #         "id": "00000000-0000-5000-8000-a10000000003", 
        #         "cat_id": "00000000-0000-3000-8000-a10000000000", 
        #         "name": "Third Party Umbrella",
        #         "description": "Third Party Umbrella",
        #         "commission": 10.00,
        #     },
        # ])

        product_cat_id = "00000000-0000-3000-8000-a10000000001"
        options = {
            'Assets All Risks': 21.00,
            'Fire and Allied Perils': 21.00,
            'Business Combined': 20.00,
            'Business Interruption': 21.00,
            'Home & Personal Assets Protection': 21.00,
            'Mobile Phone': 20.00,
            'Money Insurance (Cash in Safe)': 20.00,
            'Money Insurance (Cash in Transit)': 20.00,
            'Money Insurance (Cash Hold Up)': 20.00,
            'Pedal Cycle': 20.00
        }

        result = self.get_db_entry(options, product_cat_id, last_num)
        last_num = result['last_num']
        # db_data = []
        # for opt in options:
        #     db_data.append({
        #         "id": "00000000-0000-5000-8000-a"+str(last_num), 
        #         "cat_id": product_cat_id,
        #         "name": opt,
        #         "description": opt,
        #         "commission": options.get(opt),
        #     })
        #     print(f'Num: {last_num}', opt, options.get(opt))
        #     last_num = (last_num + 1)


        print('FIN', result['last_num'], result['data'])
        # PolicyType.bulk_create(db_data)
        

        # PolicyType.bulk_create([
        #     {
        #         "id": "00000000-0000-5000-8000-a10000000004", 
        #         "cat_id": "00000000-0000-3000-8000-a10000000001", 
        #         "name": "Assets All Risks",
        #         "description": "Assets All Risks",
        #         "commission": 21.00,
        #     },
        #     {
        #         "id": "00000000-0000-5000-8000-a10000000005", 
        #         "cat_id": "00000000-0000-3000-8000-a10000000001", 
        #         "name": "Fire and Allied Perils",
        #         "description": "Fire and Allied Perils",
        #         "commission": 21.00,
        #     },
        #     {
        #         "id": "00000000-0000-5000-8000-a10000000006", 
        #         "cat_id": "00000000-0000-3000-8000-a10000000001", 
        #         "name": "Business Combined",
        #         "description": "Business Combined",
        #         "commission": 20.00,
        #     },
        #     {
        #         "id": "00000000-0000-5000-8000-a10000000007", 
        #         "cat_id": "00000000-0000-3000-8000-a10000000001", 
        #         "name": "Business Interruption",
        #         "description": "Business Interruption",
        #         "commission": 21.00,
        #     },
        #     {
        #         "id": "00000000-0000-5000-8000-a10000000007", 
        #         "cat_id": "00000000-0000-3000-8000-a10000000001", 
        #         "name": "Business Interruption",
        #         "description": "Business Interruption",
        #         "commission": 21.00,
        #     },
        #     {
        #         "id": "00000000-0000-5000-8000-a10000000004", 
        #         "cat_id": "00000000-0000-3000-8000-a10000000003", 
        #         "name": "Marine Cargo",
        #         "description": "Marine Cargo",
        #         "commission": 15.00,
        #     },
        #     {
        #         "id": "00000000-0000-5000-8000-a10000000005", 
        #         "cat_id": "00000000-0000-3000-8000-a10000000003", 
        #         "name": "Marine Hull",
        #         "description": "Marine Hull",
        #         "commission": 15.00,
        #     },
            
        # ])

        pass


'''
"00000000-0000-3000-8000-a10000000000" - "Motor Insurance"
"00000000-0000-3000-8000-a10000000001" - "Fire & Property Damage"
"00000000-0000-3000-8000-a10000000002" - "Liability Insurance"
"00000000-0000-3000-8000-a10000000003" - "Marine & Aviation Insurance"
"00000000-0000-3000-8000-a10000000004" - "Inland Transit"
"00000000-0000-3000-8000-a10000000005" - "Engineering Insurance"
"00000000-0000-3000-8000-a10000000006" - "Health / Medical Insurance/Travel Insurance"
"00000000-0000-3000-8000-a10000000007" - "Bonds, Guarantees & Credit Insurance"
"00000000-0000-3000-8000-a10000000008" - "Agriculture Insurance"
"00000000-0000-3000-8000-a10000000009" - "Accident Insurance"


MOTOR INSURANCE	
    Motor Comprehensive	16.50%
	Motor Third Party Only	10.00%
	Motor Third Party, Fire and Theft	10.00%
	Motor Third Party Umbrella	10.00%
		
PROPERTY DAMAGE	
    Assets All Risks	21.00%
	Fire and Allied Perils	21.00%
	Business Combined	20.00%
	Business Interruption	21.00%
	Home & Personal Assets Protection	21.00%
	Mobile Phone 	20.00%
	Money Insurance (Cash in Safe)	20.00%
	Money Insurance (Cash in Transit)	20.00%
	Money Insurance (Cash Hold Up)	20.00%
	Pedal Cycle	20.00%
		
ENGINEERING	
    Contractors All Risks	20.00%
	Erection All Risks	20.00%
	Machinery Breakdown	20.00%
	Plant and Machinery	20.00%
	Electronic Equipment Insurance	20.00%
	Stock Deterioration	20.00%
	Boiler & Pressure Vessel	20.00%
		
LIFE	
    Group Life	20.00%
	Personal Life	20.00%
	Mortgage Protection	15.00%
	Credit Life	15.00%
	Group Funeral 	15.00%
	Personal Funeral 	15.00%
		
ACCIDENT	
    Group Personal Accident	20.00%
	Personal Accident	20.00%
	Workmen's Compensation	15.00%
		
LIABILITY	
    Freight Forwarders Liability	
	General Liability	20.00%
	Directors and Officers Liability	20.00%
	Public and Product Liability	20.00%
	Professional Indemnity	20.00%
	Public Liability	20.00%
	Banker Blanket Indemnity	20.00%
	Fidelity Guarantee	20.00%
	Events Liability	20.00%
	Price Insurance	20.00%
	Medical Malpractice	20.00%
	Stevedore & Shore Handling	20.00%
		
MEDICAL HEALTH	
    Group Medical Health	5.00%
	Personal Medical Health	5.00%
	Travel Insurance	10.00%
		
BONDS	
    Customs Warehouse Bond	20.00%
	Customs Removal Bond	20.00%
	Customs Temporary Importation Bond	20.00%
	Customs Exportation Bond	20.00%
	Customs Particular Bond	20.00%
	Customs Petroleum Bond	20.00%
	Performance Bond	20.00%
	Bid Bond	20.00%
	Retention Bond	20.00%
	Advanced Payment Guarantee	20.00%
	Credit Guarantee	20.00%
	Counter Guarantee	20.00%
	
TRANSIT	
    Goods In Transit	20.00%
	Marine Cargo Insurance	15.00%
	Marine Hull Insurance	15.00%
'''
    
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
