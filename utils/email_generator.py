import requests
from dotenv import load_dotenv
import json
import os
load_dotenv()

async def sendEmailwithTemplate(subject, message, template_id):
    url = "https://api.sendgrid.com/v3/mail/send" 
    key = os.getenv('SENDGRID_KEY')

    from_email = "info@ghamroonline.org"
    from_name = "Ghamro"

    try:
        payload = json.dumps({
            "personalizations": [
                {
                    "to": [
                        {
                            "email": message['email'],
                            "username":message['username']
                        }
                    ],
                   
                    "dynamic_template_data":message
                }
                #     "dynamic_template_data": {"message":message,"subject":subject}
                # }
            ],
            "template_id": template_id,
            "from": {
                "email": from_email,
                "name": from_name
            },
            "reply_to": {
                "email": from_email,
                "name": from_name
            }
        })

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + key
        }
        response = requests.post(url, headers=headers, data=payload)
       

        if response.text: # Make sure response is not empty before calling response.json()
            pass
        else:
            print("Email sent successfully")

        return {'message': 'Email dispatched successfully'}

       

    except Exception as e:
        print(str(e))
        return str(e)


