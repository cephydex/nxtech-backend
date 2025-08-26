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
                "Business Description or Trade", "Registration Number", "Make and Model of Vehicle",
                "Colour of Vehicle", "Chassis Number", "Year of Manufacture", "Sum Insured",
            ]})
        })

        ProductColumn.create({
            "id": "00000001-1200-0000-0000-a1c000000001",
            "data": json.dumps({"product_id": "00000000-0000-3000-8000-a10000000001",
            "fields": [
                "Business Description or Trade", "Description of Building", "Description of Content",
                {"Sub-Contents":["Furniture and Fittings", "Stock in Trade", "Machinery & Equipment",
                    "Computors and Accessories", "Others"]}, 
                "Locational Address of Property", "Values of Property", "Sum Insured",
            ]})
        })

        ProductColumn.create({
            "id": "00000001-1200-0000-0000-a1c000000002",
            "data": json.dumps({"product_id": "00000000-0000-3000-8000-a10000000002",
            "options": ["All Others", "Liability"],
            "fields": {
                "Liability": [
                    "Business Description or Trade", "Locations Covered", "Coverage Type (Claims Made or Claims Occurring)",
                    "Discovery Period", "Sum Insured",
                ],
                "All Others": [
                    "Business Description or Trade", "Locations Covered", "Coverage Type (Claims Made or Claims Occurring)",
                    "Discovery Period", "Sum Insured", "Professional Indemnity/Medical Malpractice/ Directors and Officers"
                ]
            }})
        })

        ProductColumn.create({
            "id": "00000000-0000-3000-8000-a1c000000003",
            "data": json.dumps({"product_id": "00000000-0000-3000-8000-a10000000003",
            "options": ["Marine Hull", "Marine Cargo"],
            "fields": {
                "Marine Hull": [
                    "Description of Vessel", "Name of Vessel", "Year of Manufacture",
                    "Flag of Vessel", "Origin of Vessel", "Destination of Vessel", "Value of Hull",
                    "Value of Machinery", "Total Value of Vessel",
                ],
                "Marine Cargo": [
                    "Description of Cargo", "Supplier’s/Commercial Invoice & Number", "Bill of Landing/Airway Bill & Number",
                    "Customs Bill of Entry (BOE) & Number", "Letter of Credit (if need be)", "Name of Vessel/Carrier",
                    "Vessel/Flight Name and Number", "Vessel Flag", "Port of Loading", "Port of Destination",
                    "Method of Packaging (Container, Bulk, Ro-Ro, Other)", "Final Destination Address (warehouse location, etc)",
                    "Sailing/Flight Date", "Estimated Arrival Date", "Transhipment Details",
                    "Value of Shipment/Consignment", "Total Estimated Carrying Value",
                ]
            }})
        })

        ProductColumn.create({
            "id": "00000000-0000-3000-8000-a1c000000004",
            "data": json.dumps({"product_id": "00000000-0000-3000-8000-a10000000004",
            "fields": [
                "Description of Goods", "Loading Location", "Destination",
                "Type of Carrying Vehicle", "Value  Per Transit", "Estimated Carrying Value",
            ]})
        })

        ProductColumn.create({
            "id": "00000000-0000-3000-8000-a1c000000005",
            "data": json.dumps({"product_id": "00000000-0000-3000-8000-a10000000005",
            "options": ["Contractors All Risks", "Erection All Risks", "All Others"],
            "fields": {
                "Contractors All Risks": [
                    "Business Description or Trade", "Description of Contract/Project",
                    "Location of Contract/Project", "Total Value of Contract",
                    "Contract Works & Materials Value", "Plant and Machinery & Value"
                    "Third Party Liability & Value", "Contract Period", "Defect Liability Period", 
                    "Name of Employer/Principal", "Name of Contractor", "Name of Sub-Contractor"
                ],
                "Erection All Risks": [
                    "Business Description or Trade", "Description of Contract/Project",
                    "Location of Contract/Project", "Total Value of Contract",
                    "Contract Works & Materials Value", "Plant and Machinery & Value"
                    "Third Party Liability & Value", "Contract Period", "Defect Liability Period", 
                    "Name of Employer/Principal", "Name of Contractor", "Name of Sub-Contractor"
                ],
                "All Others": [
                    "Business Description or Trade", "Description of Property", 
                    "Location of Property", "Total Value of Property"
                ]
            }})
        })

        ProductColumn.create({
            "id": "00000000-0000-3000-8000-a1c000000006",
            "data": json.dumps({"product_id": "00000000-0000-3000-8000-a10000000006",
            "options": ["Life", "Medical Health"],
            "fields": {
                "Life": [
                    "Business Description or Trade", "Personel Covered (Permanent Staff or Casual Staff)",
                    "Personel Covered (Clericals or Non Clericals)", "Number of Personel Covered Per Category",
                    "Average Age of Staff Covered", "Total Annual Salaries", "Capital Sum",
                ],
                "Medical Health": [
                    "Business Description or Trade", "Number of Staff", "Number of Dependants",
                    "Number of Males", "Number of Female", "Total Number of Members",
                    "In Patient Limit", "Out Patient Limit", "Optical Limit", "Dental Limit",
                    "Maternity Limit", "Pre-Existing Condition",
                ],
            }})
        })

        ProductColumn.create({
            "id": "00000000-0000-3000-8000-a1c000000007",
            "data": json.dumps({"product_id": "00000000-0000-3000-8000-a10000000007",
            "options": ["Contractual", "Customs"],
            "fields": {
                "Contractual": [
                    "Description of Contract or Trade", "Name of Principal/Employer",
                    "Name of Contractor", "Value of Contract", "Bond Amount", "Period of Bond"
                ],
                "Customs": [
                    "Business Description or Trade", "Description of Contract or Trade",
                    "Name of Principal/Employer", "Bond Amount/Value", "Period of Bond"
                ],
            }})
        })

        ProductColumn.create({
            "id": "00000000-0000-3000-8000-a1c000000008",
            "data": json.dumps({"product_id": "00000000-0000-3000-8000-a10000000009",
            "fields": [
                "Business Description or Trade", "Personel Covered (Permanent Staff or Casual Staff)",
                "Personel Covered (Clericals or Non Clericals)", "Number of Personel Covered Per Category", 
                "Total Annual Salaries",
            ]})
        })

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
