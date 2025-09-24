"""ProductColumnsTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from models.ProductColumn import ProductColumn
import json


class ProductColumnsTableSeeder(Seeder):

    def run(self):
        """Run the database seeds."""

        # {'product_id': '', 'fields': ''}
        # ProductColumn.bulk_create([ ])

        ProductColumn.create({
            "id": "00000001-1200-0000-0000-a1c000000000",
            "data": json.dumps({"product_id": "00000000-0000-3000-8000-a10000000000",
            "fields": [
                {"name":"Business Description or Trade", "type":"text", "required":"1"}, {"name":"Registration Number", "type":"string", "required":"1"}, {"name":"Make and Model of Vehicle", "type":"string", "required":"1"},
                {"name":"Colour of Vehicle", "type":"string", "required":"1"}, {"name":"Chassis Number", "type":"string", "required":"1"}, {"name":"Year of Manufacture", "type":"string", "required":"1"}, {"name":"Sum Insured", "type":"float", "required":"1"},
            ]})
        })

        ProductColumn.create({
            "id": "00000001-1200-0000-0000-a1c000000001",
            "data": json.dumps({"product_id": "00000000-0000-3000-8000-a10000000001",
            "fields": [
                {"name":"Business Description or Trade", "type":"string", "required":"1"}, {"name":"Description of Building", "type":"string", "required":"0"}, {"name":"Description of Content", "type":"text", "required":"1"},
                {"Content Options": [{"name":"Furniture and Fittings","type":"float","required":"0"},{"name":"Stock in Trade","type":"float","required":"0"},
                    {"name":"Machinery & Equipment","type":"float", "required":"0"},{"name":"Computors and Accessories", "type":"float", "required":"1"},{"name":"Others","type":"float", "required":"0"}
                ]}, 
                {"name":"Locational Address of Property","type":"string","required":"1"}, {"name":"Sum Insured","type":"float","required":"1"},
            ]})
        })

        ProductColumn.create({
            "id": "00000001-1200-0000-0000-a1c000000002",
            "data": json.dumps({"product_id": "00000000-0000-3000-8000-a10000000002",
            "options": ["All Others", "Liability"],
            "fields": {
                "Liability": [
                    {"name":"Business Description or Trade","type":"text","required":"1"},{"name":"Locations Covered", "type":"string", "required":"1"},{"name":"Coverage Type (Claims Made or Claims Occurring)","type":"string","required":"1"},
                   {"Discovery Period":"string"}, {"Sum Insured":"float"},
                ],
                "All Others": [
                    {"Business Description or Trade":"text"}, {"Locations Covered":"string"},{"Coverage Type (Claims Made or Claims Occurring)":"string"},
                    {"Discovery Period":"string"},{"Sum Insured":"float"}
                ]
            }})
        })

        ProductColumn.create({
            "id": "00000000-0000-3000-8000-a1c000000003",
            "data": json.dumps({"product_id": "00000000-0000-3000-8000-a10000000003",
            "options": ["Marine Hull", "Marine Cargo"],
            "fields": {
                "Marine Hull": [
                    {"Description of Vessel":"text"}, {"Name of Vessel":"string"}, {"Year of Manufacture":"integer"},
                    {"Flag of Vessel":"string"}, {"Origin of Vessel":"string"}, {"Destination of Vessel":"string"}, {"Value of Hull":"float"},
                    {"Value of Machinery":"float"}, {"Total Value of Vessel":"calculation"},
                ],
                "Marine Cargo": [
                    {"Description of Cargo":"text"}, {"Supplier’s/Commercial Invoice & Number":"string"}, 
                    {"Bill of Lading/Airway Bill":"file"}, {"Bill of Lading/Airway Bill Number":"string"},
                    {"Customs Bill of Entry (BOE) & Number":"string"}, {"Letter of Credit (if need be)":"file"}, "Name of Vessel/Carrier",
                    {"Vessel/Flight Name and Number":"string"}, {"Vessel Flag":"string"}, {"Port of Loading":"string"}, {"Port of Destination":"string"},
                    {"Method of Packaging (Container, Bulk, Ro-Ro, Other)":"string"}, {"Final Destination Address (warehouse location, etc)":"string"},
                    {"Sailing/Flight Date":"date"}, {"Estimated Arrival Date":"date"}, {"Transhipment Details":"text"},
                    {"Value of Shipment/Consignment":"float"}, {"Total Estimated Carrying Value":"float"},
                ]
            }})
        })

        ProductColumn.create({
            "id": "00000000-0000-3000-8000-a1c000000004",
            "data": json.dumps({"product_id": "00000000-0000-3000-8000-a10000000004",
            "fields": [
                {"Description of Goods":"text"}, {"Loading Location":"string"}, {"Destination":"string"},
                {"Type of Carrying Vehicle":"string"}, {"Value Per Transit":"float"}, {"Estimated Carrying Value":"float"},
            ]})
        })

        ProductColumn.create({
            "id": "00000000-0000-3000-8000-a1c000000005",
            "data": json.dumps({"product_id": "00000000-0000-3000-8000-a10000000005",
            "options": ["Contractors All Risks", "Erection All Risks", "All Others"],
            "fields": {
                "Contractors All Risks": [
                    {"Business Description or Trade":"string"}, {"Description of Contract/Project":"text"},
                    {"Location of Contract/Project":"string"}, {"Total Value of Contract":"float"},
                    {"Contract Works & Materials Value":"float"}, {"Plant and Machinery & Value":"float"},
                    {"Third Party Liability & Value":"float"}, {"Contract Period (Months)":"integer"}, {"Defect Liability Period":"integer"}, 
                    {"Name of Employer/Principal":"string"}, {"Name of Contractor":"string"}, {"Name of Sub-Contractor":"string"}
                ],
                "Erection All Risks": [
                    {"Business Description or Trade":"string"}, {"Description of Contract/Project":"text"},
                    {"Location of Contract/Project":"string"}, {"Total Value of Contract":"float"},
                    {"Contract Works & Materials Value":"float"}, {"Plant and Machinery & Value":"float"},
                    {"Third Party Liability & Value":"float"}, {"Contract Period (Months)":"integer"}, {"Defect Liability Period":"integer"}, 
                    {"Name of Employer/Principal":"string"}, {"Name of Contractor":"string"}, {"Name of Sub-Contractor":"string"}
                ],
                "All Others": [
                    {"Business Description or Trade":"string"}, {"Description of Property":"text"}, 
                    {"Location of Property":"string"}, {"Total Value of Property":"float"}
                ]
            }})
        })

        ProductColumn.create({
            "id": "00000000-0000-3000-8000-a1c000000006",
            "data": json.dumps({"product_id": "00000000-0000-3000-8000-a10000000006",
            "options": ["Medical Health"],
            "fields": {
                "Medical Health": [
                    {"Business Description or Trade":"string"}, {"Number of Staff":"integer"}, {"Number of Dependants":"integer"},
                    {"Number of Males":"integer"}, {"Number of Female":"integer"}, {"Total Number of Members":"integer"},
                    {"In Patient Limit":"integer"}, {"Out Patient Limit":"integer"},{"Optical Limit":"integer"}, {"Dental Limit":"integer"},
                    {"Maternity Limit":"integer"}, {"Pre-Existing Condition":"text"},
                ],
            }})
        })

        ProductColumn.create({
            "id": "00000000-0000-3000-8000-a1c000000009",
            "data": json.dumps({"product_id": "00000000-0000-3000-8000-a10000000010",
            "options": ["Life"],
            "fields": {
                "Life": [
                    {"Business Description or Trade":"text"}, {"Personel Covered (Permanent Staff)":"integer"},
                    {"Personel Covered (Casual Staff)":"integer"},{"Number of Personel Covered Per Category":"integer"},
                    {"Average Age of Staff Covered":"float"}, {"Total Annual Salaries":"float"}, {"Capital Sum":"float"},
                ]
            }})
        })

        ProductColumn.create({
            "id": "00000000-0000-3000-8000-a1c000000007",
            "data": json.dumps({"product_id": "00000000-0000-3000-8000-a10000000007",
            "options": ["Contractual", "Customs"],
            "fields": {
                "Contractual": [
                    {"Description of Contract or Trade":"text"}, {"Name of Principal/Employer":"string"},
                    {"Name of Contractor":"string"}, {"Value of Contract":"float"}, {"Bond Amount":"float"}, {"Period of Bond":"integer"}
                ],
                "Customs": [
                    {"Business Description or Trade":"text"}, {"Name of Principal/Employer":"string"},
                    {"Description of Contract":"text"},{"Bond Amount/Value":"float"}, {"Period of Bond":"integer"}
                ],
            }})
        })

        ProductColumn.create({
            "id": "00000000-0000-3000-8000-a1c000000008",
            "data": json.dumps({"product_id": "00000000-0000-3000-8000-a10000000009",
            "fields": [
                {"Business Description or Trade":"text"}, {"Personel Covered (Permanent Staff)":"integer"}, {"Personel Covered (Casual Staff)":"integer"},
                {"Personel Covered (Clericals)":"integer"},{"Personel Covered (Non Clericals)":"integer"}, {"Number of Personel Covered Per Category":"integer"}, 
                {"Total Annual Salaries":"float"},
            ]})
        })


        
        # Just for keeps
        # ProductColumn.create({
        #     "id": "00000000-0000-3000-8000-a1c000000009",
        #     "data": json.dumps({"product_id": "00000000-0000-3000-8000-a10000000010",
        #     "options": ["Life"],
        #     "fields": {
        #         "Life": [
        #             {"Business Description or Trade":"text"}, {"Personel Covered (Permanent Staff)":"integer"},{"Personel Covered (Casual Staff)":"integer"},
        #             {"Personel Covered (Clericals)":"integer"}, {"Personel Covered (Non Clericals)":"integer"}, {"Number of Personel Covered Per Category"},
        #             {"Average Age of Staff Covered":"integer"}, {"Total Annual Salaries":"float"}, {"Capital Sum":"float"},
        #         ]
        #     }})
        # })

# {"id": "00000000-0000-3000-8000-a10000000006", "name": "Health / Medical Insurance/Travel Insurance"},
# MEDICAL HEALTH
# Business Description or Trade 
# Number of Staff
# Number of Dependants
# Number of Males
# Number of Female
# Total Number of Members
# In Patient Limit
# Out Patient Limit
# Optical Limit
# Dental Limit
# Maternity Limit
# Pre-Existing Condition

# LIFE
# Business Description or Trade 
# Personel Covered (Permanent Staff or Casual Staff)
# Personel Covered (Clericals or Non Clericals)
# Number of Personel Covered Per Category
# Average Age of Staff Covered
# Total Annual Salaries
# Capital Sum


# {"id": "00000000-0000-3000-8000-a10000000001", "name": "Fire & Property Damage"},
# Business Description or Trade 
# Description of Building
# Description of Content
# Sub-Contents:
# Furniture and Fittings
# Stock in Trade
# Machinery & Equipment
# Computors and Accessories
# Others
# Locational Address of Property
# Values of Property

# {"id": "00000000-0000-3000-8000-a10000000002", "name": "Liability Insurance"},
# All Others
# Business Description or Trade *
# Locations Covered*
# Sum Insured (Limit of Indemnity)*
# Coverage Type (Claims Made or Claims Occurring)*
# Discovery Period*

# LIABILITY
# Professional Indemnity/Medical Malpractice/ Directors and Officers
# Business Description or Trade 
# Locations Covered
# Personnel Covered
# Sum Insured (Limit of Indemnity)
# Coverage Type (Claims Made or Claims Occurring)
# Discovery Period

# {"id": "00000000-0000-3000-8000-a10000000003", "name": "Marine & Aviation Insurance"},
# TRANSIT
# Marine Cargo
# Description of Cargo
# Supplier’s/Commercial Invoice & Number
# Bill of Landing/Airway Bill & Number
# Customs Bill of Entry (BOE) & Number
# Letter of Credit (if need be)
# Name of Vessel/Carrier
# Vessel/Flight Name and Number
# Vessel Flag
# Port of Loading
# Port of Destination
# Method of Packaging (Container, Bulk, Ro-Ro, Other)
# Final Destination Address (warehouse location, etc)
# Sailing/Flight Date
# Estimated Arrival Date
# Transhipment Details
# Value of Shipment/Consignment
# Total Estimated Carrying Value

# TRANSIT
# Marine Hull
# Description of Vessel
# Name of Vessel
# Year of Manufacture 
# Flag of Vessel
# Origin of Vessel
# Destination of Vessel
# Value of Hull
# Value of Machinery
# Total Value of Vessel

# {"id": "00000000-0000-3000-8000-a10000000004", "name": "Inland Transit"},

# TRANSIT
# Goods in Transit
# Description of Goods
# Loading Location
# Destination
# Type of Carrying Vehicle
# Value  Per Transit
# Estimated Carrying Value

# {"id": "00000000-0000-3000-8000-a10000000005", "name": "Engineering Insurance"},
# Contractors All Risks, Erection All Risks
# Business Description or Trade 
# Description of Contract/Project
# Location of Contract/Project
# Total Value of Contract
# Contract Works & Materials Value
# Plant and Machinery & Value
# Third Party Liability & Value
# Contract Period
# Defect Liability Period
# Name of Employer/Principal
# Name of Contractor
# Name of Sub-Contractor

# ENGINEERING
# All Others
# Business Description or Trade 
# Description of Property
# Location of Property
# Total Value of Property


# {"id": "00000000-0000-3000-8000-a10000000006", "name": "Health / Medical Insurance/Travel Insurance"},
# MEDICAL HEALTH
# Business Description or Trade 
# Number of Staff
# Number of Dependants
# Number of Males
# Number of Female
# Total Number of Members
# In Patient Limit
# Out Patient Limit
# Optical Limit
# Dental Limit
# Maternity Limit
# Pre-Existing Condition

# LIFE
# Business Description or Trade 
# Personel Covered (Permanent Staff or Casual Staff)
# Personel Covered (Clericals or Non Clericals)
# Number of Personel Covered Per Category
# Average Age of Staff Covered
# Total Annual Salaries
# Capital Sum 


# {"id": "00000000-0000-3000-8000-a10000000007", "name": "Bonds, Guarantees & Credit Insurance"},
# BONDS
# Contractual
# Business Description or Trade 
# Description of Contract or Trade
# Name of Principal/Employer
# Name of Contractor
# Value of Contract
# Bond Amount
# Period of Bond

# BONDS
# Customs
# Business Description or Trade 
# Description of Contract or Trade
# Name of Principal/Employer
# Bond Amount/Value
# Period of Bond


# {"id": "00000000-0000-3000-8000-a10000000008", "name": "Agriculture Insurance"},

# {"id": "00000000-0000-3000-8000-a10000000009", "name": "Accident Insurance"},
# Business Description or Trade 
# Personel Covered (Permanent Staff or Casual Staff)
# Personel Covered (Clericals or Non Clericals)
# Number of Personel Covered Per Category
# Total Annual Salaries

# {"id": "00000000-0000-3000-8000-a10000000010", "name": "Other"},
