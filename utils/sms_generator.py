import requests
import os
import time
import json

async def send_Sms(phone:str,message:str):
        
        url = os.getenv('WIGAL_SMS_URL')
        username = os.getenv('WIGAL_SMS_USERNAME')
        password = os.getenv('WIGAL_SMS_PASSWORD')
        sender_id = os.getenv('SMS_SENDER_ID')

        payload = {
            "username": username,
            "password": password,
            "senderid": sender_id,
            "destinations": [
                {
                    "destination": phone,
                    "msgid": int(str(time.time()).replace('.',''))
                }
            ],
            "message": message.replace('[','(').replace(']',')'),
            "service": "SMS",
            # "subject": "Hello World",
            "smstype": "text"
        }

      
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=json.dumps(payload))

        jsonResponse = response.json()

       
        code = '002'
        message = 'Failed to send sms'

        if jsonResponse['status']=='ACCEPTED':
            code = '000'
            message = 'SMS submission successful'

            print("I was sent")
    
        
        return {
            'code': code,
            'message': message
        }


