"""BanksTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from models.Bank import Bank


class BanksTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        
        Bank.bulk_create([
            {
                "id": "b0000000-fc36-0000-b000-000000000001",
                "name": "STANDARD CHARTERED BANK",
                "code": "SCH",
            },
            {
                "id": "b0000000-fc36-0000-b000-000000000002",
                "name": "ABSA BANK GHANA LIMITED",
                "code": "ABG",
            },
            {
                "id": "b0000000-fc36-0000-b000-000000000003",
                "name": "GCB BANK LIMITED",
                "code": "GCB",
            },
            {
                "id": "b0000000-fc36-0000-b000-000000000004",
                "name": "NATIONAL INVESTMENT BANK",
                "code": "NIB",
            },
            {
                "id": "b0000000-fc36-0000-b000-000000000005",
                "name": "AGRICULTURAL DEVELOPMENT BANK",
                "code": "ADB",
            },
            {
                "id": "b0000000-fc36-0000-b000-000000000006",
                "name": "UNIVERSAL MERCHANT BANK",
                "code": "UMB",
            },
            {
                "id": "b0000000-fc36-0000-b000-000000000007",
                "name": "REPUBLIC BANK LIMITED",
                "code": "RBL",
            },
            {
                "id": "b0000000-fc36-0000-b000-000000000008",
                "name": "ZENITH BANK GHANA LTD",
                "code": "ZEN",
            },
            {
                "id": "b0000000-fc36-0000-b000-000000000009",
                "name": "ECOBANK GHANA LTD",
                "code": "ECO",
            },
            {
                "id": "b0000000-fc36-0000-b000-000000000010",
                "name": "CAL BANK LIMITED",
                "code": "CAL",
            },
            {
                "id": "b0000000-fc36-0000-b000-000000000011",
                "name": "PRUDENTIAL BANK LTD",
                "code": "PRD",
            },
            {
                "id": "b0000000-fc36-0000-b000-000000000012",
                "name": "STANBIC BANK",
                "code": "STB",
            },
            {
                "id": "b0000000-fc36-0000-b000-000000000013",
                "name": "GUARANTY TRUST BANK",
                "code": "GTB",
            },
            {
                "id": "b0000000-fc36-0000-b000-000000000014",
                "name": "UNITED BANK OF AFRICA",
                "code": "UBA",
            },
            {
                "id": "b0000000-fc36-0000-b000-000000000015",
                "name": "ACCESS BANK LTD",
                "code": "ACB",
            },
            {
                "id": "b0000000-fc36-0000-b000-000000000016",
                "name": "CONSOLIDATED BANK GHANA",
                "code": "CBG",
            },
            {
                "id": "b0000000-fc36-0000-b000-000000000017",
                "name": "FIRST NATIONAL BANK",
                "code": "FNB",
            },
            {
                "id": "b0000000-fc36-0000-b000-000000000018",
                "name": "FIDELITY BANK LIMITED",
                "code": "FDB",
            },
            {
                "id": "b0000000-fc36-0000-b000-000000000019",
                "name": "GHL BANK",
                "code": "GHL",
            },
            {
                "id": "b0000000-fc36-0000-b000-000000000020",
                "name": "FIRST ATLANTIC BANK",
                "code": "FAB",
            },
            {
                "id": "b0000000-fc36-0000-b000-000000000021",
                "name": "OMNI-BSIC",
                "code": "GHL",
            },
            {
                "id": "b0000000-fc36-0000-b000-000000000022",
                "name": "SOCIETE GENERAL GHANA LTD",
                "code": "SGB",
            },
            {
                "id": "b0000000-fc36-0000-b000-000000000023",
                "name": "FIRST BANK NIGERIA",
                "code": "FBN",
            },
        ])
