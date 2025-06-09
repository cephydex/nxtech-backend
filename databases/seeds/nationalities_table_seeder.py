"""NationalitiesTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from models.Nationality import Nationality


class NationalitiesTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        
        # "num_code": "4",
        # "alpha_2_code": "AF",
        # "alpha_3_code": "AFG",
        # "short_name": "Afghanistan",
        # "nationality": "Afghan"
        
        Nationality.bulk_create([
            {
                "id": "60000000-0000-0000-0000-010000000000",
                "num_code": "4",
                "alpha_2_code": "AF",
                "alpha_3_code": "AFG",
                "short_name": "Afghanistan",
                "nationality": "Afghan"
            },
            {
                "id": "60000000-0000-0000-0000-010000000001",
                "num_code": "248",
                "alpha_2_code": "AX",
                "alpha_3_code": "ALA",
                "short_name": "\u00c5land Islands",
                "nationality": "\u00c5land Island"
            },
            {
                "id": "60000000-0000-0000-0000-010000000002",
                "num_code": "8",
                "alpha_2_code": "AL",
                "alpha_3_code": "ALB",
                "short_name": "Albania",
                "nationality": "Albanian"
            },
            {
                "id": "60000000-0000-0000-0000-010000000003",
                "num_code": "12",
                "alpha_2_code": "DZ",
                "alpha_3_code": "DZA",
                "short_name": "Algeria",
                "nationality": "Algerian"
            },
            {
                "id": "60000000-0000-0000-0000-010000000004",
                "num_code": "16",
                "alpha_2_code": "AS",
                "alpha_3_code": "ASM",
                "short_name": "American Samoa",
                "nationality": "American Samoan"
            },
            {
                "id": "60000000-0000-0000-0000-010000000005",
                "num_code": "20",
                "alpha_2_code": "AD",
                "alpha_3_code": "AND",
                "short_name": "Andorra",
                "nationality": "Andorran"
            },
            {
                "id": "60000000-0000-0000-0000-010000000006",
                "num_code": "24",
                "alpha_2_code": "AO",
                "alpha_3_code": "AGO",
                "short_name": "Angola",
                "nationality": "Angolan"
            },
            {
                "id": "60000000-0000-0000-0000-010000000007",
                "num_code": "660",
                "alpha_2_code": "AI",
                "alpha_3_code": "AIA",
                "short_name": "Anguilla",
                "nationality": "Anguillan"
            },
            {
                "id": "60000000-0000-0000-0000-010000000008",
                "num_code": "10",
                "alpha_2_code": "AQ",
                "alpha_3_code": "ATA",
                "short_name": "Antarctica",
                "nationality": "Antarctic"
            },
            {
                "id": "60000000-0000-0000-0000-010000000010",
                "num_code": "28",
                "alpha_2_code": "AG",
                "alpha_3_code": "ATG",
                "short_name": "Antigua and Barbuda",
                "nationality": "Antiguan or Barbudan"
            },
            {
                "id": "60000000-0000-0000-0000-010000000011",
                "num_code": "32",
                "alpha_2_code": "AR",
                "alpha_3_code": "ARG",
                "short_name": "Argentina",
                "nationality": "Argentine"
            },
            {
                "id": "60000000-0000-0000-0000-010000000012",
                "num_code": "51",
                "alpha_2_code": "AM",
                "alpha_3_code": "ARM",
                "short_name": "Armenia",
                "nationality": "Armenian"
            },
            {
                "id": "60000000-0000-0000-0000-010000000013",
                "num_code": "533",
                "alpha_2_code": "AW",
                "alpha_3_code": "ABW",
                "short_name": "Aruba",
                "nationality": "Aruban"
            },
            {
                "id": "60000000-0000-0000-0000-010000000014",
                "num_code": "36",
                "alpha_2_code": "AU",
                "alpha_3_code": "AUS",
                "short_name": "Australia",
                "nationality": "Australian"
            },
            {
                "id": "60000000-0000-0000-0000-010000000015",
                "num_code": "40",
                "alpha_2_code": "AT",
                "alpha_3_code": "AUT",
                "short_name": "Austria",
                "nationality": "Austrian"
            },
            {
                "id": "60000000-0000-0000-0000-010000000016",
                "num_code": "31",
                "alpha_2_code": "AZ",
                "alpha_3_code": "AZE",
                "short_name": "Azerbaijan",
                "nationality": "Azerbaijani, Azeri"
            },
            {
                "id": "60000000-0000-0000-0000-010000000017",
                "num_code": "44",
                "alpha_2_code": "BS",
                "alpha_3_code": "BHS",
                "short_name": "Bahamas",
                "nationality": "Bahamian"
            },
            {
                "id": "60000000-0000-0000-0000-010000000018",
                "num_code": "48",
                "alpha_2_code": "BH",
                "alpha_3_code": "BHR",
                "short_name": "Bahrain",
                "nationality": "Bahraini"
            },
            {
                "id": "60000000-0000-0000-0000-010000000019",
                "num_code": "50",
                "alpha_2_code": "BD",
                "alpha_3_code": "BGD",
                "short_name": "Bangladesh",
                "nationality": "Bangladeshi"
            },
            {
                "id": "60000000-0000-0000-0000-010000000020",
                "num_code": "52",
                "alpha_2_code": "BB",
                "alpha_3_code": "BRB",
                "short_name": "Barbados",
                "nationality": "Barbadian"
            },
            {
                "id": "60000000-0000-0000-0000-010000000021",
                "num_code": "112",
                "alpha_2_code": "BY",
                "alpha_3_code": "BLR",
                "short_name": "Belarus",
                "nationality": "Belarusian"
            },
            {
                "id": "60000000-0000-0000-0000-010000000022",
                "num_code": "56",
                "alpha_2_code": "BE",
                "alpha_3_code": "BEL",
                "short_name": "Belgium",
                "nationality": "Belgian"
            },
            {
                "id": "60000000-0000-0000-0000-010000000023",
                "num_code": "84",
                "alpha_2_code": "BZ",
                "alpha_3_code": "BLZ",
                "short_name": "Belize",
                "nationality": "Belizean"
            },
            {
                "id": "60000000-0000-0000-0000-010000000024",
                "num_code": "204",
                "alpha_2_code": "BJ",
                "alpha_3_code": "BEN",
                "short_name": "Benin",
                "nationality": "Beninese, Beninois"
            },
            {
                "id": "60000000-0000-0000-0000-010000000025",
                "num_code": "60",
                "alpha_2_code": "BM",
                "alpha_3_code": "BMU",
                "short_name": "Bermuda",
                "nationality": "Bermudian, Bermudan"
            },
            {
                "id": "60000000-0000-0000-0000-010000000026",
                "num_code": "64",
                "alpha_2_code": "BT",
                "alpha_3_code": "BTN",
                "short_name": "Bhutan",
                "nationality": "Bhutanese"
            },
            {
                "id": "60000000-0000-0000-0000-010000000027",
                "num_code": "68",
                "alpha_2_code": "BO",
                "alpha_3_code": "BOL",
                "short_name": "Bolivia (Plurinational State of)",
                "nationality": "Bolivian"
            },
            {
                "id": "60000000-0000-0000-0000-010000000028",
                "num_code": "535",
                "alpha_2_code": "BQ",
                "alpha_3_code": "BES",
                "short_name": "Bonaire, Sint Eustatius and Saba",
                "nationality": "Bonaire"
            },
            {
                "id": "60000000-0000-0000-0000-010000000029",
                "num_code": "70",
                "alpha_2_code": "BA",
                "alpha_3_code": "BIH",
                "short_name": "Bosnia and Herzegovina",
                "nationality": "Bosnian or Herzegovinian"
            },
            {
                "id": "60000000-0000-0000-0000-010000000030",
                "num_code": "72",
                "alpha_2_code": "BW",
                "alpha_3_code": "BWA",
                "short_name": "Botswana",
                "nationality": "Motswana, Botswanan"
            },
            {
                "id": "60000000-0000-0000-0000-010000000031",
                "num_code": "74",
                "alpha_2_code": "BV",
                "alpha_3_code": "BVT",
                "short_name": "Bouvet Island",
                "nationality": "Bouvet Island"
            },
            {
                "id": "60000000-0000-0000-0000-010000000032",
                "num_code": "76",
                "alpha_2_code": "BR",
                "alpha_3_code": "BRA",
                "short_name": "Brazil",
                "nationality": "Brazilian"
            },
            {
                "id": "60000000-0000-0000-0000-010000000033",
                "num_code": "86",
                "alpha_2_code": "IO",
                "alpha_3_code": "IOT",
                "short_name": "British Indian Ocean Territory",
                "nationality": "BIOT"
            },
            {
                "id": "60000000-0000-0000-0000-010000000034",
                "num_code": "96",
                "alpha_2_code": "BN",
                "alpha_3_code": "BRN",
                "short_name": "Brunei Darussalam",
                "nationality": "Bruneian"
            },
            {
                "id": "60000000-0000-0000-0000-010000000035",
                "num_code": "100",
                "alpha_2_code": "BG",
                "alpha_3_code": "BGR",
                "short_name": "Bulgaria",
                "nationality": "Bulgarian"
            },
            {
                "id": "60000000-0000-0000-0000-010000000036",
                "num_code": "854",
                "alpha_2_code": "BF",
                "alpha_3_code": "BFA",
                "short_name": "Burkina Faso",
                "nationality": "Burkinab\u00e9"
            },
            {
                "id": "60000000-0000-0000-0000-010000000037",
                "num_code": "108",
                "alpha_2_code": "BI",
                "alpha_3_code": "BDI",
                "short_name": "Burundi",
                "nationality": "Burundian"
            },
            {
                "id": "60000000-0000-0000-0000-010000000038",
                "num_code": "132",
                "alpha_2_code": "CV",
                "alpha_3_code": "CPV",
                "short_name": "Cabo Verde",
                "nationality": "Cabo Verdean"
            },
            {
                "id": "60000000-0000-0000-0000-010000000039",
                "num_code": "116",
                "alpha_2_code": "KH",
                "alpha_3_code": "KHM",
                "short_name": "Cambodia",
                "nationality": "Cambodian"
            },
            {
                "id": "60000000-0000-0000-0000-010000000040",
                "num_code": "120",
                "alpha_2_code": "CM",
                "alpha_3_code": "CMR",
                "short_name": "Cameroon",
                "nationality": "Cameroonian"
            },
            {
                "id": "60000000-0000-0000-0000-010000000041",
                "num_code": "124",
                "alpha_2_code": "CA",
                "alpha_3_code": "CAN",
                "short_name": "Canada",
                "nationality": "Canadian"
            },
            {
                "id": "60000000-0000-0000-0000-010000000042",
                "num_code": "136",
                "alpha_2_code": "KY",
                "alpha_3_code": "CYM",
                "short_name": "Cayman Islands",
                "nationality": "Caymanian"
            },
            {
                "id": "60000000-0000-0000-0000-010000000043",
                "num_code": "140",
                "alpha_2_code": "CF",
                "alpha_3_code": "CAF",
                "short_name": "Central African Republic",
                "nationality": "Central African"
            },
            {
                "id": "60000000-0000-0000-0000-010000000044",
                "num_code": "148",
                "alpha_2_code": "TD",
                "alpha_3_code": "TCD",
                "short_name": "Chad",
                "nationality": "Chadian"
            },
            {
                "id": "60000000-0000-0000-0000-010000000045",
                "num_code": "152",
                "alpha_2_code": "CL",
                "alpha_3_code": "CHL",
                "short_name": "Chile",
                "nationality": "Chilean"
            },
            {
                "id": "60000000-0000-0000-0000-010000000046",
                "num_code": "156",
                "alpha_2_code": "CN",
                "alpha_3_code": "CHN",
                "short_name": "China",
                "nationality": "Chinese"
            },
            {
                "id": "60000000-0000-0000-0000-010000000047",
                "num_code": "162",
                "alpha_2_code": "CX",
                "alpha_3_code": "CXR",
                "short_name": "Christmas Island",
                "nationality": "Christmas Island"
            },
            {
                "id": "60000000-0000-0000-0000-010000000048",
                "num_code": "166",
                "alpha_2_code": "CC",
                "alpha_3_code": "CCK",
                "short_name": "Cocos (Keeling) Islands",
                "nationality": "Cocos Island"
            },
            {
                "id": "60000000-0000-0000-0000-010000000049",
                "num_code": "170",
                "alpha_2_code": "CO",
                "alpha_3_code": "COL",
                "short_name": "Colombia",
                "nationality": "Colombian"
            },
            {
                "id": "60000000-0000-0000-0000-010000000050",
                "num_code": "174",
                "alpha_2_code": "KM",
                "alpha_3_code": "COM",
                "short_name": "Comoros",
                "nationality": "Comoran, Comorian"
            },
            {
                "id": "60000000-0000-0000-0000-010000000051",
                "num_code": "178",
                "alpha_2_code": "CG",
                "alpha_3_code": "COG",
                "short_name": "Congo (Republic of the)",
                "nationality": "Congolese"
            },
            {
                "id": "60000000-0000-0000-0000-010000000052",
                "num_code": "180",
                "alpha_2_code": "CD",
                "alpha_3_code": "COD",
                "short_name": "Congo (Democratic Republic of the)",
                "nationality": "Congolese"
            },
            {
                "id": "60000000-0000-0000-0000-010000000053",
                "num_code": "184",
                "alpha_2_code": "CK",
                "alpha_3_code": "COK",
                "short_name": "Cook Islands",
                "nationality": "Cook Island"
            },
            {
                "id": "60000000-0000-0000-0000-010000000054",
                "num_code": "188",
                "alpha_2_code": "CR",
                "alpha_3_code": "CRI",
                "short_name": "Costa Rica",
                "nationality": "Costa Rican"
            },
            {
                "id": "60000000-0000-0000-0000-010000000055",
                "num_code": "384",
                "alpha_2_code": "CI",
                "alpha_3_code": "CIV",
                "short_name": "C\u00f4te d'Ivoire",
                "nationality": "Ivorian"
            },
            {
                "id": "60000000-0000-0000-0000-010000000056",
                "num_code": "191",
                "alpha_2_code": "HR",
                "alpha_3_code": "HRV",
                "short_name": "Croatia",
                "nationality": "Croatian"
            },
            {
                "id": "60000000-0000-0000-0000-010000000057",
                "num_code": "192",
                "alpha_2_code": "CU",
                "alpha_3_code": "CUB",
                "short_name": "Cuba",
                "nationality": "Cuban"
            },
            {
                "id": "60000000-0000-0000-0000-010000000058",
                "num_code": "531",
                "alpha_2_code": "CW",
                "alpha_3_code": "CUW",
                "short_name": "Cura\u00e7ao",
                "nationality": "Cura\u00e7aoan"
            },
            {
                "id": "60000000-0000-0000-0000-010000000059",
                "num_code": "196",
                "alpha_2_code": "CY",
                "alpha_3_code": "CYP",
                "short_name": "Cyprus",
                "nationality": "Cypriot"
            },
            {
                "id": "60000000-0000-0000-0000-010000000060",
                "num_code": "203",
                "alpha_2_code": "CZ",
                "alpha_3_code": "CZE",
                "short_name": "Czech Republic",
                "nationality": "Czech"
            },
            {
                "id": "60000000-0000-0000-0000-010000000061",
                "num_code": "208",
                "alpha_2_code": "DK",
                "alpha_3_code": "DNK",
                "short_name": "Denmark",
                "nationality": "Danish"
            },
            {
                "id": "60000000-0000-0000-0000-010000000062",
                "num_code": "262",
                "alpha_2_code": "DJ",
                "alpha_3_code": "DJI",
                "short_name": "Djibouti",
                "nationality": "Djiboutian"
            },
            {
                "id": "60000000-0000-0000-0000-010000000063",
                "num_code": "212",
                "alpha_2_code": "DM",
                "alpha_3_code": "DMA",
                "short_name": "Dominica",
                "nationality": "Dominican"
            },
            {
                "id": "60000000-0000-0000-0000-010000000064",
                "num_code": "214",
                "alpha_2_code": "DO",
                "alpha_3_code": "DOM",
                "short_name": "Dominican Republic",
                "nationality": "Dominican"
            },
            {
                "id": "60000000-0000-0000-0000-010000000065",
                "num_code": "218",
                "alpha_2_code": "EC",
                "alpha_3_code": "ECU",
                "short_name": "Ecuador",
                "nationality": "Ecuadorian"
            },
            {
                "id": "60000000-0000-0000-0000-010000000066",
                "num_code": "818",
                "alpha_2_code": "EG",
                "alpha_3_code": "EGY",
                "short_name": "Egypt",
                "nationality": "Egyptian"
            },
            {
                "id": "60000000-0000-0000-0000-010000000067",
                "num_code": "222",
                "alpha_2_code": "SV",
                "alpha_3_code": "SLV",
                "short_name": "El Salvador",
                "nationality": "Salvadoran"
            },
            {
                "id": "60000000-0000-0000-0000-010000000068",
                "num_code": "226",
                "alpha_2_code": "GQ",
                "alpha_3_code": "GNQ",
                "short_name": "Equatorial Guinea",
                "nationality": "Equatorial Guinean, Equatoguinean"
            },
            {
                "id": "60000000-0000-0000-0000-010000000069",
                "num_code": "232",
                "alpha_2_code": "ER",
                "alpha_3_code": "ERI",
                "short_name": "Eritrea",
                "nationality": "Eritrean"
            },
            {
                "id": "60000000-0000-0000-0000-010000000070",
                "num_code": "233",
                "alpha_2_code": "EE",
                "alpha_3_code": "EST",
                "short_name": "Estonia",
                "nationality": "Estonian"
            },
            {
                "id": "60000000-0000-0000-0000-010000000071",
                "num_code": "231",
                "alpha_2_code": "ET",
                "alpha_3_code": "ETH",
                "short_name": "Ethiopia",
                "nationality": "Ethiopian"
            },
            {
                "id": "60000000-0000-0000-0000-010000000072",
                "num_code": "238",
                "alpha_2_code": "FK",
                "alpha_3_code": "FLK",
                "short_name": "Falkland Islands (Malvinas)",
                "nationality": "Falkland Island"
            },
            {
                "id": "60000000-0000-0000-0000-010000000073",
                "num_code": "234",
                "alpha_2_code": "FO",
                "alpha_3_code": "FRO",
                "short_name": "Faroe Islands",
                "nationality": "Faroese"
            },
            {
                "id": "60000000-0000-0000-0000-010000000074",
                "num_code": "242",
                "alpha_2_code": "FJ",
                "alpha_3_code": "FJI",
                "short_name": "Fiji",
                "nationality": "Fijian"
            },
            {
                "id": "60000000-0000-0000-0000-010000000075",
                "num_code": "246",
                "alpha_2_code": "FI",
                "alpha_3_code": "FIN",
                "short_name": "Finland",
                "nationality": "Finnish"
            },
            {
                "id": "60000000-0000-0000-0000-010000000076",
                "num_code": "250",
                "alpha_2_code": "FR",
                "alpha_3_code": "FRA",
                "short_name": "France",
                "nationality": "French"
            },
            {
                "id": "60000000-0000-0000-0000-010000000077",
                "num_code": "254",
                "alpha_2_code": "GF",
                "alpha_3_code": "GUF",
                "short_name": "French Guiana",
                "nationality": "French Guianese"
            },
            {
                "id": "60000000-0000-0000-0000-010000000078",
                "num_code": "258",
                "alpha_2_code": "PF",
                "alpha_3_code": "PYF",
                "short_name": "French Polynesia",
                "nationality": "French Polynesian"
            },
            {
                "id": "60000000-0000-0000-0000-010000000079",
                "num_code": "260",
                "alpha_2_code": "TF",
                "alpha_3_code": "ATF",
                "short_name": "French Southern Territories",
                "nationality": "French Southern Territories"
            },
            {
                "id": "60000000-0000-0000-0000-010000000080",
                "num_code": "266",
                "alpha_2_code": "GA",
                "alpha_3_code": "GAB",
                "short_name": "Gabon",
                "nationality": "Gabonese"
            },
            {
                "id": "60000000-0000-0000-0000-010000000081",
                "num_code": "270",
                "alpha_2_code": "GM",
                "alpha_3_code": "GMB",
                "short_name": "Gambia",
                "nationality": "Gambian"
            },
            {
                "id": "60000000-0000-0000-0000-010000000082",
                "num_code": "268",
                "alpha_2_code": "GE",
                "alpha_3_code": "GEO",
                "short_name": "Georgia",
                "nationality": "Georgian"
            },
            {
                "id": "60000000-0000-0000-0000-010000000083",
                "num_code": "276",
                "alpha_2_code": "DE",
                "alpha_3_code": "DEU",
                "short_name": "Germany",
                "nationality": "German"
            },
            {
                "id": "60000000-0000-0000-0000-010000000084",
                "num_code": "288",
                "alpha_2_code": "GH",
                "alpha_3_code": "GHA",
                "short_name": "Ghana",
                "nationality": "Ghanaian"
            },
            {
                "id": "60000000-0000-0000-0000-010000000085",
                "num_code": "292",
                "alpha_2_code": "GI",
                "alpha_3_code": "GIB",
                "short_name": "Gibraltar",
                "nationality": "Gibraltar"
            },
            {
                "id": "60000000-0000-0000-0000-010000000086",
                "num_code": "300",
                "alpha_2_code": "GR",
                "alpha_3_code": "GRC",
                "short_name": "Greece",
                "nationality": "Greek, Hellenic"
            },
            {
                "id": "60000000-0000-0000-0000-010000000087",
                "num_code": "304",
                "alpha_2_code": "GL",
                "alpha_3_code": "GRL",
                "short_name": "Greenland",
                "nationality": "Greenlandic"
            },
            {
                "id": "60000000-0000-0000-0000-010000000088",
                "num_code": "308",
                "alpha_2_code": "GD",
                "alpha_3_code": "GRD",
                "short_name": "Grenada",
                "nationality": "Grenadian"
            },
            {
                "id": "60000000-0000-0000-0000-010000000089",
                "num_code": "312",
                "alpha_2_code": "GP",
                "alpha_3_code": "GLP",
                "short_name": "Guadeloupe",
                "nationality": "Guadeloupe"
            },
            {
                "id": "60000000-0000-0000-0000-010000000090",
                "num_code": "316",
                "alpha_2_code": "GU",
                "alpha_3_code": "GUM",
                "short_name": "Guam",
                "nationality": "Guamanian, Guambat"
            },
            {
                "id": "60000000-0000-0000-0000-010000000091",
                "num_code": "320",
                "alpha_2_code": "GT",
                "alpha_3_code": "GTM",
                "short_name": "Guatemala",
                "nationality": "Guatemalan"
            },
            {
                "id": "60000000-0000-0000-0000-010000000092",
                "num_code": "831",
                "alpha_2_code": "GG",
                "alpha_3_code": "GGY",
                "short_name": "Guernsey",
                "nationality": "Channel Island"
            },
            {
                "id": "60000000-0000-0000-0000-010000000093",
                "num_code": "324",
                "alpha_2_code": "GN",
                "alpha_3_code": "GIN",
                "short_name": "Guinea",
                "nationality": "Guinean"
            },
            {
                "id": "60000000-0000-0000-0000-010000000094",
                "num_code": "624",
                "alpha_2_code": "GW",
                "alpha_3_code": "GNB",
                "short_name": "Guinea-Bissau",
                "nationality": "Bissau-Guinean"
            },
            {
                "id": "60000000-0000-0000-0000-010000000095",
                "num_code": "328",
                "alpha_2_code": "GY",
                "alpha_3_code": "GUY",
                "short_name": "Guyana",
                "nationality": "Guyanese"
            },
            {
                "id": "60000000-0000-0000-0000-010000000096",
                "num_code": "332",
                "alpha_2_code": "HT",
                "alpha_3_code": "HTI",
                "short_name": "Haiti",
                "nationality": "Haitian"
            },
            {
                "id": "60000000-0000-0000-0000-010000000097",
                "num_code": "334",
                "alpha_2_code": "HM",
                "alpha_3_code": "HMD",
                "short_name": "Heard Island and McDonald Islands",
                "nationality": "Heard Island or McDonald Islands"
            },
            {
                "id": "60000000-0000-0000-0000-010000000098",
                "num_code": "336",
                "alpha_2_code": "VA",
                "alpha_3_code": "VAT",
                "short_name": "Vatican City State",
                "nationality": "Vatican"
            },
            {
                "id": "60000000-0000-0000-0000-010000000099",
                "num_code": "340",
                "alpha_2_code": "HN",
                "alpha_3_code": "HND",
                "short_name": "Honduras",
                "nationality": "Honduran"
            },
            {
                "id": "60000000-0000-0000-0000-010000000100",
                "num_code": "344",
                "alpha_2_code": "HK",
                "alpha_3_code": "HKG",
                "short_name": "Hong Kong",
                "nationality": "Hong Kong, Hong Kongese"
            },
            {
                "id": "60000000-0000-0000-0000-010000000101",
                "num_code": "348",
                "alpha_2_code": "HU",
                "alpha_3_code": "HUN",
                "short_name": "Hungary",
                "nationality": "Hungarian, Magyar"
            },
            {
                "id": "60000000-0000-0000-0000-010000000102",
                "num_code": "352",
                "alpha_2_code": "IS",
                "alpha_3_code": "ISL",
                "short_name": "Iceland",
                "nationality": "Icelandic"
            },
            {
                "id": "60000000-0000-0000-0000-010000000103",
                "num_code": "356",
                "alpha_2_code": "IN",
                "alpha_3_code": "IND",
                "short_name": "India",
                "nationality": "Indian"
            },
            {
                "id": "60000000-0000-0000-0000-010000000104",
                "num_code": "360",
                "alpha_2_code": "ID",
                "alpha_3_code": "IDN",
                "short_name": "Indonesia",
                "nationality": "Indonesian"
            },
            {
                "id": "60000000-0000-0000-0000-010000000105",
                "num_code": "364",
                "alpha_2_code": "IR",
                "alpha_3_code": "IRN",
                "short_name": "Iran",
                "nationality": "Iranian, Persian"
            },
            {
                "id": "60000000-0000-0000-0000-010000000106",
                "num_code": "368",
                "alpha_2_code": "IQ",
                "alpha_3_code": "IRQ",
                "short_name": "Iraq",
                "nationality": "Iraqi"
            },
            {
                "id": "60000000-0000-0000-0000-010000000107",
                "num_code": "372",
                "alpha_2_code": "IE",
                "alpha_3_code": "IRL",
                "short_name": "Ireland",
                "nationality": "Irish"
            },
            {
                "id": "60000000-0000-0000-0000-010000000108",
                "num_code": "833",
                "alpha_2_code": "IM",
                "alpha_3_code": "IMN",
                "short_name": "Isle of Man",
                "nationality": "Manx"
            },
            {
                "id": "60000000-0000-0000-0000-010000000109",
                "num_code": "376",
                "alpha_2_code": "IL",
                "alpha_3_code": "ISR",
                "short_name": "Israel",
                "nationality": "Israeli"
            },
            {
                "id": "60000000-0000-0000-0000-010000000110",
                "num_code": "380",
                "alpha_2_code": "IT",
                "alpha_3_code": "ITA",
                "short_name": "Italy",
                "nationality": "Italian"
            },
            {
                "id": "60000000-0000-0000-0000-010000000111",
                "num_code": "388",
                "alpha_2_code": "JM",
                "alpha_3_code": "JAM",
                "short_name": "Jamaica",
                "nationality": "Jamaican"
            },
            {
                "id": "60000000-0000-0000-0000-010000000112",
                "num_code": "392",
                "alpha_2_code": "JP",
                "alpha_3_code": "JPN",
                "short_name": "Japan",
                "nationality": "Japanese"
            },
            {
                "id": "60000000-0000-0000-0000-010000000113",
                "num_code": "832",
                "alpha_2_code": "JE",
                "alpha_3_code": "JEY",
                "short_name": "Jersey",
                "nationality": "Channel Island"
            },
            {
                "id": "60000000-0000-0000-0000-010000000114",
                "num_code": "400",
                "alpha_2_code": "JO",
                "alpha_3_code": "JOR",
                "short_name": "Jordan",
                "nationality": "Jordanian"
            },
            {
                "id": "60000000-0000-0000-0000-010000000115",
                "num_code": "398",
                "alpha_2_code": "KZ",
                "alpha_3_code": "KAZ",
                "short_name": "Kazakhstan",
                "nationality": "Kazakhstani, Kazakh"
            },
            {
                "id": "60000000-0000-0000-0000-010000000116",
                "num_code": "404",
                "alpha_2_code": "KE",
                "alpha_3_code": "KEN",
                "short_name": "Kenya",
                "nationality": "Kenyan"
            },
            {
                "id": "60000000-0000-0000-0000-010000000117",
                "num_code": "296",
                "alpha_2_code": "KI",
                "alpha_3_code": "KIR",
                "short_name": "Kiribati",
                "nationality": "I-Kiribati"
            },
            {
                "id": "60000000-0000-0000-0000-010000000118",
                "num_code": "408",
                "alpha_2_code": "KP",
                "alpha_3_code": "PRK",
                "short_name": "Korea (Democratic People's Republic of)",
                "nationality": "North Korean"
            },
            {
                "id": "60000000-0000-0000-0000-010000000119",
                "num_code": "410",
                "alpha_2_code": "KR",
                "alpha_3_code": "KOR",
                "short_name": "Korea (Republic of)",
                "nationality": "South Korean"
            },
            {
                "id": "60000000-0000-0000-0000-010000000120",
                "num_code": "414",
                "alpha_2_code": "KW",
                "alpha_3_code": "KWT",
                "short_name": "Kuwait",
                "nationality": "Kuwaiti"
            },
            {
                "id": "60000000-0000-0000-0000-010000000121",
                "num_code": "417",
                "alpha_2_code": "KG",
                "alpha_3_code": "KGZ",
                "short_name": "Kyrgyzstan",
                "nationality": "Kyrgyzstani, Kyrgyz, Kirgiz, Kirghiz"
            },
            {
                "id": "60000000-0000-0000-0000-010000000122",
                "num_code": "418",
                "alpha_2_code": "LA",
                "alpha_3_code": "LAO",
                "short_name": "Lao People's Democratic Republic",
                "nationality": "Lao, Laotian"
            },
            {
                "id": "60000000-0000-0000-0000-010000000123",
                "num_code": "428",
                "alpha_2_code": "LV",
                "alpha_3_code": "LVA",
                "short_name": "Latvia",
                "nationality": "Latvian"
            },
            {
                "id": "60000000-0000-0000-0000-010000000124",
                "num_code": "422",
                "alpha_2_code": "LB",
                "alpha_3_code": "LBN",
                "short_name": "Lebanon",
                "nationality": "Lebanese"
            },
            {
                "id": "60000000-0000-0000-0000-010000000125",
                "num_code": "426",
                "alpha_2_code": "LS",
                "alpha_3_code": "LSO",
                "short_name": "Lesotho",
                "nationality": "Basotho"
            },
            {
                "id": "60000000-0000-0000-0000-010000000126",
                "num_code": "430",
                "alpha_2_code": "LR",
                "alpha_3_code": "LBR",
                "short_name": "Liberia",
                "nationality": "Liberian"
            },
            {
                "id": "60000000-0000-0000-0000-010000000127",
                "num_code": "434",
                "alpha_2_code": "LY",
                "alpha_3_code": "LBY",
                "short_name": "Libya",
                "nationality": "Libyan"
            },
            {
                "id": "60000000-0000-0000-0000-010000000128",
                "num_code": "438",
                "alpha_2_code": "LI",
                "alpha_3_code": "LIE",
                "short_name": "Liechtenstein",
                "nationality": "Liechtenstein"
            },
            {
                "id": "60000000-0000-0000-0000-010000000129",
                "num_code": "440",
                "alpha_2_code": "LT",
                "alpha_3_code": "LTU",
                "short_name": "Lithuania",
                "nationality": "Lithuanian"
            },
            {
                "id": "60000000-0000-0000-0000-010000000130",
                "num_code": "442",
                "alpha_2_code": "LU",
                "alpha_3_code": "LUX",
                "short_name": "Luxembourg",
                "nationality": "Luxembourg, Luxembourgish"
            },
            {
                "id": "60000000-0000-0000-0000-010000000131",
                "num_code": "446",
                "alpha_2_code": "MO",
                "alpha_3_code": "MAC",
                "short_name": "Macao",
                "nationality": "Macanese, Chinese"
            },
            {
                "id": "60000000-0000-0000-0000-010000000132",
                "num_code": "807",
                "alpha_2_code": "MK",
                "alpha_3_code": "MKD",
                "short_name": "Macedonia (the former Yugoslav Republic of)",
                "nationality": "Macedonian"
            },
            {
                "id": "60000000-0000-0000-0000-010000000133",
                "num_code": "450",
                "alpha_2_code": "MG",
                "alpha_3_code": "MDG",
                "short_name": "Madagascar",
                "nationality": "Malagasy"
            },
            {
                "id": "60000000-0000-0000-0000-010000000134",
                "num_code": "454",
                "alpha_2_code": "MW",
                "alpha_3_code": "MWI",
                "short_name": "Malawi",
                "nationality": "Malawian"
            },
            {
                "id": "60000000-0000-0000-0000-010000000135",
                "num_code": "458",
                "alpha_2_code": "MY",
                "alpha_3_code": "MYS",
                "short_name": "Malaysia",
                "nationality": "Malaysian"
            },
            {
                "id": "60000000-0000-0000-0000-010000000136",
                "num_code": "462",
                "alpha_2_code": "MV",
                "alpha_3_code": "MDV",
                "short_name": "Maldives",
                "nationality": "Maldivian"
            },
            {
                "id": "60000000-0000-0000-0000-010000000137",
                "num_code": "466",
                "alpha_2_code": "ML",
                "alpha_3_code": "MLI",
                "short_name": "Mali",
                "nationality": "Malian, Malinese"
            },
            {
                "id": "60000000-0000-0000-0000-010000000138",
                "num_code": "470",
                "alpha_2_code": "MT",
                "alpha_3_code": "MLT",
                "short_name": "Malta",
                "nationality": "Maltese"
            },
            {
                "id": "60000000-0000-0000-0000-010000000139",
                "num_code": "584",
                "alpha_2_code": "MH",
                "alpha_3_code": "MHL",
                "short_name": "Marshall Islands",
                "nationality": "Marshallese"
            },
            {
                "id": "60000000-0000-0000-0000-010000000140",
                "num_code": "474",
                "alpha_2_code": "MQ",
                "alpha_3_code": "MTQ",
                "short_name": "Martinique",
                "nationality": "Martiniquais, Martinican"
            },
            {
                "id": "60000000-0000-0000-0000-010000000141",
                "num_code": "478",
                "alpha_2_code": "MR",
                "alpha_3_code": "MRT",
                "short_name": "Mauritania",
                "nationality": "Mauritanian"
            },
            {
                "id": "60000000-0000-0000-0000-010000000142",
                "num_code": "480",
                "alpha_2_code": "MU",
                "alpha_3_code": "MUS",
                "short_name": "Mauritius",
                "nationality": "Mauritian"
            },
            {
                "id": "60000000-0000-0000-0000-010000000143",
                "num_code": "175",
                "alpha_2_code": "YT",
                "alpha_3_code": "MYT",
                "short_name": "Mayotte",
                "nationality": "Mahoran"
            },
            {
                "id": "60000000-0000-0000-0000-010000000144",
                "num_code": "484",
                "alpha_2_code": "MX",
                "alpha_3_code": "MEX",
                "short_name": "Mexico",
                "nationality": "Mexican"
            },
            {
                "id": "60000000-0000-0000-0000-010000000145",
                "num_code": "583",
                "alpha_2_code": "FM",
                "alpha_3_code": "FSM",
                "short_name": "Micronesia (Federated States of)",
                "nationality": "Micronesian"
            },
            {
                "id": "60000000-0000-0000-0000-010000000146",
                "num_code": "498",
                "alpha_2_code": "MD",
                "alpha_3_code": "MDA",
                "short_name": "Moldova (Republic of)",
                "nationality": "Moldovan"
            },
            {
                "id": "60000000-0000-0000-0000-010000000147",
                "num_code": "492",
                "alpha_2_code": "MC",
                "alpha_3_code": "MCO",
                "short_name": "Monaco",
                "nationality": "Mon\u00e9gasque, Monacan"
            },
            {
                "id": "60000000-0000-0000-0000-010000000148",
                "num_code": "496",
                "alpha_2_code": "MN",
                "alpha_3_code": "MNG",
                "short_name": "Mongolia",
                "nationality": "Mongolian"
            },
            {
                "id": "60000000-0000-0000-0000-010000000149",
                "num_code": "499",
                "alpha_2_code": "ME",
                "alpha_3_code": "MNE",
                "short_name": "Montenegro",
                "nationality": "Montenegrin"
            },
            {
                "id": "60000000-0000-0000-0000-010000000150",
                "num_code": "500",
                "alpha_2_code": "MS",
                "alpha_3_code": "MSR",
                "short_name": "Montserrat",
                "nationality": "Montserratian"
            },
            {
                "id": "60000000-0000-0000-0000-010000000151",
                "num_code": "504",
                "alpha_2_code": "MA",
                "alpha_3_code": "MAR",
                "short_name": "Morocco",
                "nationality": "Moroccan"
            },
            {
                "id": "60000000-0000-0000-0000-010000000152",
                "num_code": "508",
                "alpha_2_code": "MZ",
                "alpha_3_code": "MOZ",
                "short_name": "Mozambique",
                "nationality": "Mozambican"
            },
            {
                "id": "60000000-0000-0000-0000-010000000153",
                "num_code": "104",
                "alpha_2_code": "MM",
                "alpha_3_code": "MMR",
                "short_name": "Myanmar",
                "nationality": "Burmese"
            },
            {
                "id": "60000000-0000-0000-0000-010000000154",
                "num_code": "516",
                "alpha_2_code": "NA",
                "alpha_3_code": "NAM",
                "short_name": "Namibia",
                "nationality": "Namibian"
            },
            {
                "id": "60000000-0000-0000-0000-010000000155",
                "num_code": "520",
                "alpha_2_code": "NR",
                "alpha_3_code": "NRU",
                "short_name": "Nauru",
                "nationality": "Nauruan"
            },
            {
                "id": "60000000-0000-0000-0000-010000000156",
                "num_code": "524",
                "alpha_2_code": "NP",
                "alpha_3_code": "NPL",
                "short_name": "Nepal",
                "nationality": "Nepali, Nepalese"
            },
            {
                "id": "60000000-0000-0000-0000-010000000157",
                "num_code": "528",
                "alpha_2_code": "NL",
                "alpha_3_code": "NLD",
                "short_name": "Netherlands",
                "nationality": "Dutch, Netherlandic"
            },
            {
                "id": "60000000-0000-0000-0000-010000000158",
                "num_code": "540",
                "alpha_2_code": "NC",
                "alpha_3_code": "NCL",
                "short_name": "New Caledonia",
                "nationality": "New Caledonian"
            },
            {
                "id": "60000000-0000-0000-0000-010000000159",
                "num_code": "554",
                "alpha_2_code": "NZ",
                "alpha_3_code": "NZL",
                "short_name": "New Zealand",
                "nationality": "New Zealand, NZ"
            },
            {
                "id": "60000000-0000-0000-0000-010000000160",
                "num_code": "558",
                "alpha_2_code": "NI",
                "alpha_3_code": "NIC",
                "short_name": "Nicaragua",
                "nationality": "Nicaraguan"
            },
            {
                "id": "60000000-0000-0000-0000-010000000161",
                "num_code": "562",
                "alpha_2_code": "NE",
                "alpha_3_code": "NER",
                "short_name": "Niger",
                "nationality": "Nigerien"
            },
            {
                "id": "60000000-0000-0000-0000-010000000162",
                "num_code": "566",
                "alpha_2_code": "NG",
                "alpha_3_code": "NGA",
                "short_name": "Nigeria",
                "nationality": "Nigerian"
            },
            {
                "id": "60000000-0000-0000-0000-010000000163",
                "num_code": "570",
                "alpha_2_code": "NU",
                "alpha_3_code": "NIU",
                "short_name": "Niue",
                "nationality": "Niuean"
            },
            {
                "id": "60000000-0000-0000-0000-010000000164",
                "num_code": "574",
                "alpha_2_code": "NF",
                "alpha_3_code": "NFK",
                "short_name": "Norfolk Island",
                "nationality": "Norfolk Island"
            },
            {
                "id": "60000000-0000-0000-0000-010000000165",
                "num_code": "580",
                "alpha_2_code": "MP",
                "alpha_3_code": "MNP",
                "short_name": "Northern Mariana Islands",
                "nationality": "Northern Marianan"
            },
            {
                "id": "60000000-0000-0000-0000-010000000166",
                "num_code": "578",
                "alpha_2_code": "NO",
                "alpha_3_code": "NOR",
                "short_name": "Norway",
                "nationality": "Norwegian"
            },
            {
                "id": "60000000-0000-0000-0000-010000000167",
                "num_code": "512",
                "alpha_2_code": "OM",
                "alpha_3_code": "OMN",
                "short_name": "Oman",
                "nationality": "Omani"
            },
            {
                "id": "60000000-0000-0000-0000-010000000168",
                "num_code": "586",
                "alpha_2_code": "PK",
                "alpha_3_code": "PAK",
                "short_name": "Pakistan",
                "nationality": "Pakistani"
            },
            {
                "id": "60000000-0000-0000-0000-010000000169",
                "num_code": "585",
                "alpha_2_code": "PW",
                "alpha_3_code": "PLW",
                "short_name": "Palau",
                "nationality": "Palauan"
            },
            {
                "id": "60000000-0000-0000-0000-010000000170",
                "num_code": "275",
                "alpha_2_code": "PS",
                "alpha_3_code": "PSE",
                "short_name": "Palestine, State of",
                "nationality": "Palestinian"
            },
            {
                "id": "60000000-0000-0000-0000-010000000171",
                "num_code": "591",
                "alpha_2_code": "PA",
                "alpha_3_code": "PAN",
                "short_name": "Panama",
                "nationality": "Panamanian"
            },
            {
                "id": "60000000-0000-0000-0000-010000000172",
                "num_code": "598",
                "alpha_2_code": "PG",
                "alpha_3_code": "PNG",
                "short_name": "Papua New Guinea",
                "nationality": "Papua New Guinean, Papuan"
            },
            {
                "id": "60000000-0000-0000-0000-010000000173",
                "num_code": "600",
                "alpha_2_code": "PY",
                "alpha_3_code": "PRY",
                "short_name": "Paraguay",
                "nationality": "Paraguayan"
            },
            {
                "id": "60000000-0000-0000-0000-010000000174",
                "num_code": "604",
                "alpha_2_code": "PE",
                "alpha_3_code": "PER",
                "short_name": "Peru",
                "nationality": "Peruvian"
            },
            {
                "id": "60000000-0000-0000-0000-010000000175",
                "num_code": "608",
                "alpha_2_code": "PH",
                "alpha_3_code": "PHL",
                "short_name": "Philippines",
                "nationality": "Philippine, Filipino"
            },
            {
                "id": "60000000-0000-0000-0000-010000000176",
                "num_code": "612",
                "alpha_2_code": "PN",
                "alpha_3_code": "PCN",
                "short_name": "Pitcairn",
                "nationality": "Pitcairn Island"
            },
            {
                "id": "60000000-0000-0000-0000-010000000177",
                "num_code": "616",
                "alpha_2_code": "PL",
                "alpha_3_code": "POL",
                "short_name": "Poland",
                "nationality": "Polish"
            },
            {
                "id": "60000000-0000-0000-0000-010000000178",
                "num_code": "620",
                "alpha_2_code": "PT",
                "alpha_3_code": "PRT",
                "short_name": "Portugal",
                "nationality": "Portuguese"
            },
            {
                "id": "60000000-0000-0000-0000-010000000179",
                "num_code": "630",
                "alpha_2_code": "PR",
                "alpha_3_code": "PRI",
                "short_name": "Puerto Rico",
                "nationality": "Puerto Rican"
            },
            {
                "id": "60000000-0000-0000-0000-010000000180",
                "num_code": "634",
                "alpha_2_code": "QA",
                "alpha_3_code": "QAT",
                "short_name": "Qatar",
                "nationality": "Qatari"
            },
            {
                "id": "60000000-0000-0000-0000-010000000181",
                "num_code": "638",
                "alpha_2_code": "RE",
                "alpha_3_code": "REU",
                "short_name": "R\u00e9union",
                "nationality": "R\u00e9unionese, R\u00e9unionnais"
            },
            {
                "id": "60000000-0000-0000-0000-010000000182",
                "num_code": "642",
                "alpha_2_code": "RO",
                "alpha_3_code": "ROU",
                "short_name": "Romania",
                "nationality": "Romanian"
            },
            {
                "id": "60000000-0000-0000-0000-010000000183",
                "num_code": "643",
                "alpha_2_code": "RU",
                "alpha_3_code": "RUS",
                "short_name": "Russian Federation",
                "nationality": "Russian"
            },
            {
                "id": "60000000-0000-0000-0000-010000000184",
                "num_code": "646",
                "alpha_2_code": "RW",
                "alpha_3_code": "RWA",
                "short_name": "Rwanda",
                "nationality": "Rwandan"
            },
            {
                "id": "60000000-0000-0000-0000-010000000185",
                "num_code": "652",
                "alpha_2_code": "BL",
                "alpha_3_code": "BLM",
                "short_name": "Saint Barth\u00e9lemy",
                "nationality": "Barth\u00e9lemois"
            },
            {
                "id": "60000000-0000-0000-0000-010000000186",
                "num_code": "654",
                "alpha_2_code": "SH",
                "alpha_3_code": "SHN",
                "short_name": "Saint Helena, Ascension and Tristan da Cunha",
                "nationality": "Saint Helenian"
            },
            {
                "id": "60000000-0000-0000-0000-010000000187",
                "num_code": "659",
                "alpha_2_code": "KN",
                "alpha_3_code": "KNA",
                "short_name": "Saint Kitts and Nevis",
                "nationality": "Kittitian or Nevisian"
            },
            {
                "id": "60000000-0000-0000-0000-010000000188",
                "num_code": "662",
                "alpha_2_code": "LC",
                "alpha_3_code": "LCA",
                "short_name": "Saint Lucia",
                "nationality": "Saint Lucian"
            },
            {
                "id": "60000000-0000-0000-0000-010000000189",
                "num_code": "663",
                "alpha_2_code": "MF",
                "alpha_3_code": "MAF",
                "short_name": "Saint Martin (French part)",
                "nationality": "Saint-Martinoise"
            },
            {
                "id": "60000000-0000-0000-0000-010000000190",
                "num_code": "666",
                "alpha_2_code": "PM",
                "alpha_3_code": "SPM",
                "short_name": "Saint Pierre and Miquelon",
                "nationality": "Saint-Pierrais or Miquelonnais"
            },
            {
                "id": "60000000-0000-0000-0000-010000000191",
                "num_code": "670",
                "alpha_2_code": "VC",
                "alpha_3_code": "VCT",
                "short_name": "Saint Vincent and the Grenadines",
                "nationality": "Saint Vincentian, Vincentian"
            },
            {
                "id": "60000000-0000-0000-0000-010000000192",
                "num_code": "882",
                "alpha_2_code": "WS",
                "alpha_3_code": "WSM",
                "short_name": "Samoa",
                "nationality": "Samoan"
            },
            {
                "id": "60000000-0000-0000-0000-010000000193",
                "num_code": "674",
                "alpha_2_code": "SM",
                "alpha_3_code": "SMR",
                "short_name": "San Marino",
                "nationality": "Sammarinese"
            },
            {
                "id": "60000000-0000-0000-0000-010000000194",
                "num_code": "678",
                "alpha_2_code": "ST",
                "alpha_3_code": "STP",
                "short_name": "Sao Tome and Principe",
                "nationality": "S\u00e3o Tom\u00e9an"
            },
            {
                "id": "60000000-0000-0000-0000-010000000195",
                "num_code": "682",
                "alpha_2_code": "SA",
                "alpha_3_code": "SAU",
                "short_name": "Saudi Arabia",
                "nationality": "Saudi, Saudi Arabian"
            },
            {
                "id": "60000000-0000-0000-0000-010000000196",
                "num_code": "686",
                "alpha_2_code": "SN",
                "alpha_3_code": "SEN",
                "short_name": "Senegal",
                "nationality": "Senegalese"
            },
            {
                "id": "60000000-0000-0000-0000-010000000197",
                "num_code": "688",
                "alpha_2_code": "RS",
                "alpha_3_code": "SRB",
                "short_name": "Serbia",
                "nationality": "Serbian"
            },
            {
                "id": "60000000-0000-0000-0000-010000000198",
                "num_code": "690",
                "alpha_2_code": "SC",
                "alpha_3_code": "SYC",
                "short_name": "Seychelles",
                "nationality": "Seychellois"
            },
            {
                "id": "60000000-0000-0000-0000-010000000199",
                "num_code": "694",
                "alpha_2_code": "SL",
                "alpha_3_code": "SLE",
                "short_name": "Sierra Leone",
                "nationality": "Sierra Leonean"
            },
            {
                "id": "60000000-0000-0000-0000-010000000200",
                "num_code": "702",
                "alpha_2_code": "SG",
                "alpha_3_code": "SGP",
                "short_name": "Singapore",
                "nationality": "Singaporean"
            },
            {
                "id": "60000000-0000-0000-0000-010000000201",
                "num_code": "534",
                "alpha_2_code": "SX",
                "alpha_3_code": "SXM",
                "short_name": "Sint Maarten (Dutch part)",
                "nationality": "Sint Maarten"
            },
            {
                "id": "60000000-0000-0000-0000-010000000202",
                "num_code": "703",
                "alpha_2_code": "SK",
                "alpha_3_code": "SVK",
                "short_name": "Slovakia",
                "nationality": "Slovak"
            },
            {
                "id": "60000000-0000-0000-0000-010000000203",
                "num_code": "705",
                "alpha_2_code": "SI",
                "alpha_3_code": "SVN",
                "short_name": "Slovenia",
                "nationality": "Slovenian, Slovene"
            },
            {
                "id": "60000000-0000-0000-0000-010000000204",
                "num_code": "90",
                "alpha_2_code": "SB",
                "alpha_3_code": "SLB",
                "short_name": "Solomon Islands",
                "nationality": "Solomon Island"
            },
            {
                "id": "60000000-0000-0000-0000-010000000205",
                "num_code": "706",
                "alpha_2_code": "SO",
                "alpha_3_code": "SOM",
                "short_name": "Somalia",
                "nationality": "Somali, Somalian"
            },
            {
                "id": "60000000-0000-0000-0000-010000000206",
                "num_code": "710",
                "alpha_2_code": "ZA",
                "alpha_3_code": "ZAF",
                "short_name": "South Africa",
                "nationality": "South African"
            },
            {
                "id": "60000000-0000-0000-0000-010000000207",
                "num_code": "239",
                "alpha_2_code": "GS",
                "alpha_3_code": "SGS",
                "short_name": "South Georgia and the South Sandwich Islands",
                "nationality": "South Georgia or South Sandwich Islands"
            },
            {
                "id": "60000000-0000-0000-0000-010000000208",
                "num_code": "728",
                "alpha_2_code": "SS",
                "alpha_3_code": "SSD",
                "short_name": "South Sudan",
                "nationality": "South Sudanese"
            },
            {
                "id": "60000000-0000-0000-0000-010000000209",
                "num_code": "724",
                "alpha_2_code": "ES",
                "alpha_3_code": "ESP",
                "short_name": "Spain",
                "nationality": "Spanish"
            },
            {
                "id": "60000000-0000-0000-0000-010000000210",
                "num_code": "144",
                "alpha_2_code": "LK",
                "alpha_3_code": "LKA",
                "short_name": "Sri Lanka",
                "nationality": "Sri Lankan"
            },
            {
                "id": "60000000-0000-0000-0000-010000000211",
                "num_code": "729",
                "alpha_2_code": "SD",
                "alpha_3_code": "SDN",
                "short_name": "Sudan",
                "nationality": "Sudanese"
            },
            {
                "id": "60000000-0000-0000-0000-010000000212",
                "num_code": "740",
                "alpha_2_code": "SR",
                "alpha_3_code": "SUR",
                "short_name": "Suriname",
                "nationality": "Surinamese"
            },
            {
                "id": "60000000-0000-0000-0000-010000000213",
                "num_code": "744",
                "alpha_2_code": "SJ",
                "alpha_3_code": "SJM",
                "short_name": "Svalbard and Jan Mayen",
                "nationality": "Svalbard"
            },
            {
                "id": "60000000-0000-0000-0000-010000000214",
                "num_code": "748",
                "alpha_2_code": "SZ",
                "alpha_3_code": "SWZ",
                "short_name": "Swaziland",
                "nationality": "Swazi"
            },
            {
                "id": "60000000-0000-0000-0000-010000000215",
                "num_code": "752",
                "alpha_2_code": "SE",
                "alpha_3_code": "SWE",
                "short_name": "Sweden",
                "nationality": "Swedish"
            },
            {
                "id": "60000000-0000-0000-0000-010000000216",
                "num_code": "756",
                "alpha_2_code": "CH",
                "alpha_3_code": "CHE",
                "short_name": "Switzerland",
                "nationality": "Swiss"
            },
            {
                "id": "60000000-0000-0000-0000-010000000217",
                "num_code": "760",
                "alpha_2_code": "SY",
                "alpha_3_code": "SYR",
                "short_name": "Syrian Arab Republic",
                "nationality": "Syrian"
            },
            {
                "id": "60000000-0000-0000-0000-010000000218",
                "num_code": "158",
                "alpha_2_code": "TW",
                "alpha_3_code": "TWN",
                "short_name": "Taiwan, Province of China",
                "nationality": "Chinese, Taiwanese"
            },
            {
                "id": "60000000-0000-0000-0000-010000000219",
                "num_code": "762",
                "alpha_2_code": "TJ",
                "alpha_3_code": "TJK",
                "short_name": "Tajikistan",
                "nationality": "Tajikistani"
            },
            {
                "id": "60000000-0000-0000-0000-010000000220",
                "num_code": "834",
                "alpha_2_code": "TZ",
                "alpha_3_code": "TZA",
                "short_name": "Tanzania, United Republic of",
                "nationality": "Tanzanian"
            },
            {
                "id": "60000000-0000-0000-0000-010000000221",
                "num_code": "764",
                "alpha_2_code": "TH",
                "alpha_3_code": "THA",
                "short_name": "Thailand",
                "nationality": "Thai"
            },
            {
                "id": "60000000-0000-0000-0000-010000000222",
                "num_code": "626",
                "alpha_2_code": "TL",
                "alpha_3_code": "TLS",
                "short_name": "Timor-Leste",
                "nationality": "Timorese"
            },
            {
                "id": "60000000-0000-0000-0000-010000000223",
                "num_code": "768",
                "alpha_2_code": "TG",
                "alpha_3_code": "TGO",
                "short_name": "Togo",
                "nationality": "Togolese"
            },
            {
                "id": "60000000-0000-0000-0000-010000000224",
                "num_code": "772",
                "alpha_2_code": "TK",
                "alpha_3_code": "TKL",
                "short_name": "Tokelau",
                "nationality": "Tokelauan"
            },
            {
                "id": "60000000-0000-0000-0000-010000000225",
                "num_code": "776",
                "alpha_2_code": "TO",
                "alpha_3_code": "TON",
                "short_name": "Tonga",
                "nationality": "Tongan"
            },
            {
                "id": "60000000-0000-0000-0000-010000000226",
                "num_code": "780",
                "alpha_2_code": "TT",
                "alpha_3_code": "TTO",
                "short_name": "Trinidad and Tobago",
                "nationality": "Trinidadian or Tobagonian"
            },
            {
                "id": "60000000-0000-0000-0000-010000000227",
                "num_code": "788",
                "alpha_2_code": "TN",
                "alpha_3_code": "TUN",
                "short_name": "Tunisia",
                "nationality": "Tunisian"
            },
            {
                "id": "60000000-0000-0000-0000-010000000228",
                "num_code": "792",
                "alpha_2_code": "TR",
                "alpha_3_code": "TUR",
                "short_name": "Turkey",
                "nationality": "Turkish"
            },
            {
                "id": "60000000-0000-0000-0000-010000000229",
                "num_code": "795",
                "alpha_2_code": "TM",
                "alpha_3_code": "TKM",
                "short_name": "Turkmenistan",
                "nationality": "Turkmen"
            },
            {
                "id": "60000000-0000-0000-0000-010000000230",
                "num_code": "796",
                "alpha_2_code": "TC",
                "alpha_3_code": "TCA",
                "short_name": "Turks and Caicos Islands",
                "nationality": "Turks and Caicos Island"
            },
            {
                "id": "60000000-0000-0000-0000-010000000231",
                "num_code": "798",
                "alpha_2_code": "TV",
                "alpha_3_code": "TUV",
                "short_name": "Tuvalu",
                "nationality": "Tuvaluan"
            },
            {
                "id": "60000000-0000-0000-0000-010000000232",
                "num_code": "800",
                "alpha_2_code": "UG",
                "alpha_3_code": "UGA",
                "short_name": "Uganda",
                "nationality": "Ugandan"
            },
            {
                "id": "60000000-0000-0000-0000-010000000234",
                "num_code": "804",
                "alpha_2_code": "UA",
                "alpha_3_code": "UKR",
                "short_name": "Ukraine",
                "nationality": "Ukrainian"
            },
            {
                "id": "60000000-0000-0000-0000-010000000235",
                "num_code": "784",
                "alpha_2_code": "AE",
                "alpha_3_code": "ARE",
                "short_name": "United Arab Emirates",
                "nationality": "Emirati, Emirian, Emiri"
            },
            {
                "id": "60000000-0000-0000-0000-010000000236",
                "num_code": "826",
                "alpha_2_code": "GB",
                "alpha_3_code": "GBR",
                "short_name": "United Kingdom of Great Britain and Northern Ireland",
                "nationality": "British, UK"
            },
            {
                "id": "60000000-0000-0000-0000-010000000237",
                "num_code": "581",
                "alpha_2_code": "UM",
                "alpha_3_code": "UMI",
                "short_name": "United States Minor Outlying Islands",
                "nationality": "American"
            },
            {
                "id": "60000000-0000-0000-0000-010000000238",
                "num_code": "840",
                "alpha_2_code": "US",
                "alpha_3_code": "USA",
                "short_name": "United States of America",
                "nationality": "American"
            },
            {
                "id": "60000000-0000-0000-0000-010000000239",
                "num_code": "858",
                "alpha_2_code": "UY",
                "alpha_3_code": "URY",
                "short_name": "Uruguay",
                "nationality": "Uruguayan"
            },
            {
                "id": "60000000-0000-0000-0000-010000000240",
                "num_code": "860",
                "alpha_2_code": "UZ",
                "alpha_3_code": "UZB",
                "short_name": "Uzbekistan",
                "nationality": "Uzbekistani, Uzbek"
            },
            {
                "id": "60000000-0000-0000-0000-010000000241",
                "num_code": "548",
                "alpha_2_code": "VU",
                "alpha_3_code": "VUT",
                "short_name": "Vanuatu",
                "nationality": "Ni-Vanuatu, Vanuatuan"
            },
            {
                "id": "60000000-0000-0000-0000-010000000242",
                "num_code": "862",
                "alpha_2_code": "VE",
                "alpha_3_code": "VEN",
                "short_name": "Venezuela (Bolivarian Republic of)",
                "nationality": "Venezuelan"
            },
            {
                "id": "60000000-0000-0000-0000-010000000243",
                "num_code": "704",
                "alpha_2_code": "VN",
                "alpha_3_code": "VNM",
                "short_name": "Vietnam",
                "nationality": "Vietnamese"
            },
            {
                "id": "60000000-0000-0000-0000-010000000244",
                "num_code": "92",
                "alpha_2_code": "VG",
                "alpha_3_code": "VGB",
                "short_name": "Virgin Islands (British)",
                "nationality": "British Virgin Island"
            },
            {
                "id": "60000000-0000-0000-0000-010000000245",
                "num_code": "850",
                "alpha_2_code": "VI",
                "alpha_3_code": "VIR",
                "short_name": "Virgin Islands (U.S.)",
                "nationality": "U.S. Virgin Island"
            },
            {
                "id": "60000000-0000-0000-0000-010000000246",
                "num_code": "876",
                "alpha_2_code": "WF",
                "alpha_3_code": "WLF",
                "short_name": "Wallis and Futuna",
                "nationality": "Wallis and Futuna, Wallisian or Futunan"
            },
            {
                "id": "60000000-0000-0000-0000-010000000247",
                "num_code": "732",
                "alpha_2_code": "EH",
                "alpha_3_code": "ESH",
                "short_name": "Western Sahara",
                "nationality": "Sahrawi, Sahrawian, Sahraouian"
            },
            {
                "id": "60000000-0000-0000-0000-010000000248",
                "num_code": "887",
                "alpha_2_code": "YE",
                "alpha_3_code": "YEM",
                "short_name": "Yemen",
                "nationality": "Yemeni"
            },
            {
                "id": "60000000-0000-0000-0000-010000000249",
                "num_code": "894",
                "alpha_2_code": "ZM",
                "alpha_3_code": "ZMB",
                "short_name": "Zambia",
                "nationality": "Zambian"
            },
            {
                "id": "60000000-0000-0000-0000-010000000250",
                "num_code": "716",
                "alpha_2_code": "ZW",
                "alpha_3_code": "ZWE",
                "short_name": "Zimbabwe",
                "nationality": "Zimbabwean"
            }
        ])
        
        pass
