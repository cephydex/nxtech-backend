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
            # print(f'Num: {last_num}', opt, options.get(opt))
            last_num = (last_num + 1)
        
        return {'data': db_data, 'last_num': last_num}


    def run(self):
        """Run the database seeds."""

        # print('LAST ID', self.getInitId("00000000-0000-5000-8000-a10000000000"))
        print('\n')
        last_num:int = self.getInitId("00000000-0000-5000-8000-a10000000000")

        # product_cat_id = "00000000-0000-3000-8000-a10000000000"
        options = {
            'Comprehensive': 16.50,
            'Third Party Only': 10.00,
            'Third Party, Fire and Theft': 10.00,
            'Third Party Umbrella': 10.00,
        }
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

        result = self.get_db_entry(options, "00000000-0000-3000-8000-a10000000000", last_num)
        last_num = result['last_num']
        db_data = result['data']
        PolicyType.bulk_create(db_data)
        
        # product_cat_id = "00000000-0000-3000-8000-a10000000001"
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

        result = self.get_db_entry(options, "00000000-0000-3000-8000-a10000000001", last_num)
        last_num = result['last_num']
        db_data = result['data']
        PolicyType.bulk_create(db_data)
        # print('FIN', last_num, db_data)

        # LIABILITY
        options = {
            'Freight Forwarders Liability': 20.00,
            'General Liability':	20.00,
            'Directors and Officers Liability': 20.00,
            'Public and Product Liability': 20.00,
            'Professional Indemnity': 20.00,
            'Public Liability': 20.00,
            'Banker Blanket Indemnity': 20.00,
            'Fidelity Guarantee': 20.00,
            'Events Liability': 20.00,
            'Price Insurance': 20.00,
            'Medical Malpractice': 20.00,
            'Stevedore & Shore Handling': 20.00,
        }
        result = self.get_db_entry(options, "00000000-0000-3000-8000-a10000000002", last_num)
        last_num = result['last_num']
        db_data = result['data']
        PolicyType.bulk_create(db_data)

        # MARINE
        options = {
            'Marine Cargo Insurance': 15.00,
            'Marine Hull Insurance': 15.00
        }	
        result = self.get_db_entry(options, "00000000-0000-3000-8000-a10000000003", last_num)
        last_num = result['last_num']
        db_data = result['data']
        PolicyType.bulk_create(db_data)

        # TRANSIT
        options = {
            'Goods In Transit': 20.00,
        }	
        result = self.get_db_entry(options, "00000000-0000-3000-8000-a10000000004", last_num)
        last_num = result['last_num']
        db_data = result['data']
        PolicyType.bulk_create(db_data)
        

        # ENGINEERING
        options = {
            'Contractors All Risks':	20.00,
            'Erection All Risks': 20.00,
            'Machinery Breakdown': 20.00,
            'Plant and Machinery': 20.00,
            'Electronic Equipment Insurance': 20.00,
            'Stock Deterioration': 20.00,
            'Boiler & Pressure Vessel': 20.00
        }
        result = self.get_db_entry(options, "00000000-0000-3000-8000-a10000000005", last_num)
        last_num = result['last_num']
        db_data = result['data']
        PolicyType.bulk_create(db_data)

        # MEDICAL HEALTH	
        options = {
            'Group Medical Health': 5.00,
            'Personal Medical Health': 5.00,
            'Travel Insurance': 10.00,
        }
        result = self.get_db_entry(options, "00000000-0000-3000-8000-a10000000006", last_num)
        last_num = result['last_num']
        db_data = result['data']
        PolicyType.bulk_create(db_data)
		
        # BONDS	
        options = {
            'Customs Warehouse Bond': 20.00,
            'Customs Removal Bond': 20.00,
            'Customs Temporary Importation Bond': 20.00,
            'Customs Exportation Bond': 20.00,
            'Customs Particular Bond': 20.00,
            'Customs Petroleum Bond': 20.00,
            'Performance Bond': 20.00,
            'Bid Bond': 20.00,
            'Retention Bond': 20.00,
            'Advanced Payment Guarantee': 20.00,
            'Credit Guarantee': 20.00,
            'Counter Guarantee': 20.00,
        }
        result = self.get_db_entry(options, "00000000-0000-3000-8000-a10000000007", last_num)
        last_num = result['last_num']
        db_data = result['data']
        PolicyType.bulk_create(db_data)
		
        # AGRIC	
        options = {
            'Multi Peril Crop': 10.00,
            'Multi Peril Livestock': 10.00,
            'Index Insurance': 10.00,
        }
        result = self.get_db_entry(options, "00000000-0000-3000-8000-a10000000008", last_num)
        last_num = result['last_num']
        db_data = result['data']
        PolicyType.bulk_create(db_data)

        # ACCIDENT	
        options = {
            'Group Personal Accident': 20.00,
            'Personal Accident': 20.00,
            "Workmen's Compensation": 15.00
        }
        result = self.get_db_entry(options, "00000000-0000-3000-8000-a10000000009", last_num)
        last_num = result['last_num']
        db_data = result['data']
        PolicyType.bulk_create(db_data)

        # LIFE	
        options = {
            'Group Life': 20.00,
           ' Personal Life': 20.00,
            'Mortgage Protection': 15.00,
            'Credit Life': 15.00,
            'Group Funeral': 15.00,
            'Personal Funeral': 15.00,
        }
        result = self.get_db_entry(options, "00000000-0000-3000-8000-a10000000010", last_num)
        last_num = result['last_num']
        db_data = result['data']
        PolicyType.bulk_create(db_data)

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
"00000000-0000-3000-8000-a10000000010" - "Life Insurance"

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

MARINE
	Marine Cargo Insurance	15.00%
	Marine Hull Insurance	15.00%
'''

