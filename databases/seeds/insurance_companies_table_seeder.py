"""InsuranceCompaniesTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from models.InsuranceCompany import InsuranceCompany


class InsuranceCompaniesTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""

        InsuranceCompany.bulk_create([
            {
                "id": "c000000c-fc36-4000-a000-000000000001",
                "name": "Starlife Assurance Company Limited",
                "head_office_addr": "P.O. Box AN 5783 , Accra – North Ghana",
                "contact_no": '233302739600',
                # "email": 'info@starlifeassurance.com',
            },
            {
                "id": "c000000c-fc36-4000-a000-000000000002",
                "name": "SIC Life Company Limited",
                "head_office_addr": "P. O. Box CT3242	No. 1 Jones Nelson Road, Adabraka Freetown, Accra",
                "contact_no": '233302750151',
                # "email": 'info@siclife.com'
            },		
            {
                "id": "c000000c-fc36-4000-a000-000000000003",
                "name": "Saham Life Insurance Ghana Limited",
                "head_office_addr": "Accra",
                "contact_no": '233570000000',
                # "email": 'info@sahaminsurance.com.gh',
            },
            {
                "id": "c000000c-fc36-4000-a000-000000000004",
                "name": "Prudential Life Insurance Ghana",
                "head_office_addr": "Accra",
                "contact_no": '233302208877',
                # "email": 'info@prudential.com.gh'
            },
            {
                "id": "c000000c-fc36-4000-a000-000000000005",
                "name": "Quality Life Assurance Company Limited",
                "head_office_addr": "Accra",
                "contact_no": '233200000000',
                # "email": 'info@qlagh.com',
            },	
            {
                "id": "c000000c-fc36-4000-a000-000000000006",
                "name": "Phoenix Life Assurance Company",
                "head_office_addr": "Accra",
                "contact_no": '233200000000',
                # "email": 'info@assurance.cdhgroup.co'
            },	
            {
                "id": "c000000c-fc36-4000-a000-000000000007",
                "name": "Old Mutual Life Assurance Company Ghana",
                "head_office_addr": "Accra",
                "contact_no": '233200000001',
                # "email": 'info@oldmutual.com.gh',
            },	
            {
                "id": "c000000c-fc36-4000-a000-000000000008",
                "name": "MiLife Company Company Limited",
                "head_office_addr": "Accra",
                "contact_no": '233200000002',
                # "email": 'info@milifeghana.com'
            },
            {
                "id": "c000000c-fc36-4000-a000-000000000009",
                "name": "Hollard Life Assurance Company Limited",
                "head_office_addr": "Accra",
                "contact_no": '233200000004',
                # "email": 'info@hollard.co.za',
            },	
            {
                "id": "c000000c-fc36-4000-a000-000000000010",
                "name": "GN Life Assurance Limited",
                "head_office_addr": "Accra",
                "contact_no": '233200000005',
                # "email": 'info@gnlifeassurance.com'
            },
            {
                "id": "c000000c-fc36-4000-a000-000000000011",
                "name": "Glico Life Insurance Company",
                "head_office_addr": "Accraa",
                "contact_no": '233200000006',
                # "email": 'info@glicolife.com',
            },	
            {
                "id": "c000000c-fc36-4000-a000-000000000012",
                "name": "Ghana Life Insurance Company",
                "head_office_addr": "Accra",
                "contact_no": '233200000008',
                # "email": 'info@ghalife.com'
            },	
            {
                "id": "c000000c-fc36-4000-a000-000000000013",
                "name": "Esich Life Assurance Company Ltd.",
                "head_office_addr": "Accra",
                "contact_no": '233200000011',
                # "email": 'info@esichlife.com',
            },	
            {
                "id": "c000000c-fc36-4000-a000-000000000014",
                "name": "Enterprise Life Assurance LTD",
                "head_office_addr": "Accra",
                "contact_no": '233200000012',
                # "email": 'info@enterpriselife.com'
            },	
            {
                "id": "c000000c-fc36-4000-a000-000000000015",
                "name": "Donewell Life Company",
                "head_office_addr": "Accra",
                "contact_no": '233200000013',
                # "email": 'info@donewell.com',
            },	
            {
                "id": "c000000c-fc36-4000-a000-000000000016",
                "name": "Beige Assure Company",
                "head_office_addr": "Accra",
                "contact_no": '233200000014',
                # "email": 'info@beigeassure.com'
            },	
            {
                "id": "c000000c-fc36-4000-a000-000000000017",
                "name": "Allianz Life Insurance Ghana Limited",
                "head_office_addr": "Accra",
                "contact_no": '233200000015',
                # "email": 'info@allianzlife.com',
            },	
            {
                "id": "c000000c-fc36-4000-a000-000000000018",
                "name": "Vanguard Life Assurance Company Limited",
                "head_office_addr": "No.25 Independence Avenue, Ridge-Accra",
                "contact_no": '233244334407',
                # "email": 'info@vanguardassurance.com'
            },
        ])
