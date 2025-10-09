import os, logging
from dotenv import load_dotenv
# from requests.structures import CaseInsensitiveDict
# from python_graphql_client import GraphqlClient
# from sqlalchemy.orm import Session, sessionmaker
# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from enum import Enum as PyEnum
import requests

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
# from datetime import datetime, timedelta
from pytz import timezone


load_dotenv()
logger = logging.getLogger()

# database_url = os.getenv('DATABASE_URL')
# engine = create_engine(database_url)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base()
# Base.metadata.create_all(bind=engine)

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

class Utils:

    def calculate_month_addition(months:int = 12):
        # date = datetime(2025, 9, 24)
        date = datetime.now().date()
        # Add months
        return date + relativedelta(months=months)

    
    def compareDates(date_str):
        tz = timezone('UTC')
        currentDate = datetime.now(tz)
        
        try:
            # Parse the provided date string into a datetime object
            target_dateTime = datetime.fromisoformat(date_str)
        
        except ValueError:
            # Handle the case where the date_str cannot be parsed
            return False
        
        time_diff = currentDate - target_dateTime

        time_threshold = timedelta(minutes=10)
    
        if time_diff > time_threshold:
            return True
        
        return False



class GQL:
    
    def __init__(self, *args, **kwargs):
        # super(CLASS_NAME, self).__init__(*args, **kwargs)
        self.__url:str = os.getenv('HASURA_GRAPHQL_URL')
        self.__token:str = os.getenv('HASURA_GRAPHQL_TOKEN')
        self.__headers:str = CaseInsensitiveDict()
        
        self.__headers["content-type"] = "application/json"
        self.__headers[os.getenv("HASURA_GRAPHQL_SECRET")] = self.__token


    def graphql_client(self, query:str, variables:dict) -> dict:
        client = GraphqlClient(endpoint=self.__url, headers=self.__headers)
        data: dict = client.execute(query=query, variables=variables)

        return data



class Hubtel:
    # HUBTEL_PAYMENT_URL=https://payproxyapi.hubtel.com/items/initiate
    # HUBTEL_PAYMENT_STATUS_URL=https://api-txnstatus.hubtel.com/transactions
    # HUBTEL_CALLBACK_URL=https://backend.staging.mypolicy.market/external/hubtel/callback
    # HUBTEL_MERCHANT_ACCOUNT_NO="2016727"
    # HUBTEL_PAYMENT_AUTH_TOKEN
    
    def __init__(self) -> None:
        self.__base_url__ = os.getenv("APP_BASE_URL")
        self.__client_id__ = os.getenv("HUBTEL_CLIENT_ID")
        self.__client_secret__ = os.getenv("HUBTEL_CLIENT_SECRET")
        self.__auth_token__ = os.getenv("HUBTEL_AUTH_TOKEN")
        self.__merchant_acc_no__ = os.getenv("HUBTEL_MERCHANT_ACCOUNT_NO")
        self.__prepaid_deposit_id__ = os.getenv("HUBTEL_PREPAID_DEPOSIT_ID")
        self.__checkout_url__ = os.getenv("HUBTEL_CHECKOUT_URL")
        self.__momo_url__ = os.getenv("HUBTEL_MOMO_URL")
        self.__bank_url__ = os.getenv("HUBTEL_BANK_URL")


    def initiate_prompt(self, phone_no, amount, client_reference, description, channel = 'mtn-gh'):
        # merchant_account_no = os.getenv("HUBTEL_MERCHANT_ACCOUNT_NO")
        # auth_token = self.__auth_token__
        # url = f"https://rmp.hubtel.com/merchantaccount/merchants/2016799/receive/mobilemoney"
        # url = f"https://rmp.hubtel.com/merchantaccount/merchants/{self.__merchant_acc_no__}/receive/mobilemoney"
        url = f"https://proxy.omnistrategies.net/merchantaccount/merchants/{self.__merchant_acc_no__}/receive/mobilemoney"
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "authorization": f"Basic {self.__auth_token__}",
        }
        
        payload = {            
            "clientReference": client_reference,
            'customerMsisdn': phone_no,
            'channel': channel,
            'amount': amount,
            'primaryCallbackUrl': self.__base_url__,
            'description': description,
            'accountNumber': phone_no,
            'transactionType': "receive",
            'paymentChannel': "mtn",
        }            
    
        res_data = requests.post(url, json=payload, headers=headers)        
        if res_data.status_code != 200:
            raise Exception(f"Hubtel API - Initiate payment :: {res_data.status_code} - {res_data.text}")        

        return res_data.json()


    def initiate_payment(self, amount, client_reference, description, return_url):
        url = f"{self.__checkout_url__}/items/initiate"

        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "authorization": f"Basic {self.__auth_token__}",
        }

        payload = {
            "totalAmount": amount,
            "description": description,
            "callbackUrl": f"{self.__base_url__}/payments/initiate_callback",
            "cancellationUrl": f"{self.__base_url__}/payments/initiate_cancellation",
            "returnUrl": return_url,
            "merchantAccountNumber": self.__merchant_acc_no__,
            "clientReference": client_reference,
        }

        res = requests.post(url, json=payload, headers=headers)        
        if res.status_code != 200:
            raise Exception(f"Hubtel API - Initiate payment :: {res.status_code} - {res.text}")

        return res.json()
    

    def send_to_bank(self, amount, bank_name, bank_code, bank_acc_no, client_reference, description):
        url = f"{self.__bank_url__}/api/merchants/{self.__prepaid_deposit_id__}/send/bank/gh/{bank_code}"
        
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "authorization": f"Basic {self.__auth_token__}",
        }
        # logger.warn(url)
        # payload = {
        #     "Amount": amount,
        #     "BankAccountNumber": bank_acc_no,
        #     "ClientReference": client_reference,
        #     "PrimaryCallbackUrl": f"{self.__base_url__}/payments/bank_callback",
        #     "Description": description
        # }

        payload = { 
            "Amount": amount,
            "BankName": bank_name,
            "BankBranch": "",
            "BankBranchCode": "",
            "BankAccountNumber": bank_acc_no,
            # "BankAccountName": bank_name,
            "BankAccountName": "",
            "ClientReference": client_reference,
            "PrimaryCallbackUrl": f"{self.__base_url__}/payments/bank_callback",
            "Description": description,
            "RecipientPhoneNumber": ""
        }
        logger.warning(payload)

        res = requests.post(url, json=payload, headers=headers)        
        if res.status_code != 200:
            raise Exception(f"Hubtel API - Send to bank :: {res.status_code} - {res.text}")

        return res.json()


    def send_to_momo(self):
        pass


    def send_to_bank_status(self, clientRef: str):
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "authorization": f"Basic {self.__auth_token__}",
        }
        url = f"https://smrsc.hubtel.com/api/merchants/{self.__prepaid_deposit_id__}/transactions/status?clientReference={clientRef}"

        res = requests.get(url, headers=headers)
        if res.status_code != 200:
            raise Exception(f"Hubtel API - Send to bank status check :: {res.status_code} - {res.text}")

        return res.json()
