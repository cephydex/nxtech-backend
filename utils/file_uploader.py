from fastapi import File, UploadFile, HTTPException
import boto3
from dotenv import load_dotenv
load_dotenv()
import uuid
import os
import base64
import io


s3_client = boto3.client('s3',
                    aws_access_key_id = os.getenv('S3_ACCESS_KEY_ID'),
                    aws_secret_access_key = os.getenv('S3_SECRET_ACCESS_KEY'),
                    region_name="eu-west-3"
                     )


unsigned_s3_client=boto3.client(
    's3',
    aws_access_key_id = os.getenv('S3_ACCESS_KEY_ID'),
    aws_secret_access_key = os.getenv('S3_SECRET_ACCESS_KEY'),
    region_name="eu-west-3"
    
)

unsigned_s3_client._request_signer.sign = (lambda *args, **kwargs: None)
BUCKET_NAME=os.getenv('BUCKET_NAME')


def uploadmyfile(file, key):
    try:
        # Generate a unique file name by combining the 'key' and file extension
        file_extension = os.path.splitext(file.filename)[1]
        file_name = f'{uuid.uuid4().hex}-{key}{file_extension}'
        
        # Save the file to a temporary location
        with open(f'/tmp/{file_name}', 'wb+') as destination:
            for chunk in file.file:
                destination.write(chunk)

        # Upload the file to the specified S3 bucket
        s3_client.upload_file(
            f'/tmp/{file_name}',
            BUCKET_NAME,
            f'Ghamro/{file_name}'
        )

        resp = {
            'message': f'{file_name} is successfully uploaded into {BUCKET_NAME}',
            'data': file_name,
            'code': 200
        }

        return resp
    except Exception as exc:
        return {
            'message': 'Error occurred during file upload',
            'error_details': str(exc),
            'code': 500
        }



def getImageUrl(objname):
    try:
        url = unsigned_s3_client.generate_presigned_url(
            'get_object',
            Params={
                'Bucket': BUCKET_NAME,
                'Key': 'Ghamro/' + objname
            }
          
        )
        resp = {
            'message': 'Resource found',
            'download_url': url,
        }
        return resp                    
    except Exception as exc:
        return "Error occurred: " + str(exc)
    
async def uploadBase64file(base64File,file_name=None):

    try:
        if not file_name:
            file_name = f'{uuid.uuid4().hex}.png'

    
        file_in_bytes=base64.b64decode(base64File)


        file_as_stream = io.BytesIO(file_in_bytes)


        with open('/tmp/'+file_name, 'wb+') as destination:
            for chunk in file_as_stream:
                destination.write(chunk)
                
        s3_client.upload_file(
                "/tmp/"+file_name, BUCKET_NAME, "Ghamro/"+file_name
        )
        # s3_client.upload_fileobj(file_as_stream, bucketname, 'MegaFortune/'+file_name)

        resp={
            'message':file_name+' is successfully uploaded into '+BUCKET_NAME,
            'data':file_name,
            'code':200
        }

        print(resp)

      

        return resp
    except Exception as e:
        print(str(e))


# c=uploadBase64file("Y3VzdG9tZXIvZnVsbF9uYW1lLGN1c3RvbWVyL3Bob25lX251bWJlcixwaWNrcy8wLHBpY2tzLzEsc3Rha2Vfc3RhdHVzLHN0YWtlX3R5cGUsc3Rha2VkX2Ftb3VudCxwYXltZW50L3N0YXR1cyxwaWNrcy8yLHBpY2tzLzMNCkxlb24gIEFtcGFoLDIzMzUwMTIxMjMyOSwxNSwxMixsb3NlLE1lZ2EtMiwxLHBhaWQsLA0KR29kc3dheSBLd2FiaW5hICBNb2R6YWthLDIzMzUzMDY0Nzc4Nyw1OSw4MCx3b24sTWVnYS0yLDIscGFpZCwsDQpTb2xvbW9uICAgTGV0c2EsMjMzMjQ5MzcwNjQzLDI0LDYyLGxvc2UsTWVnYS0yLDQscGFpZCwsDQpTb2xvbW9uICAgTGV0c2EsMjMzMjQ5MzcwNjQzLDMwLDMzLHdvbixNZWdhLTMsNixwYWlkLDM0LA0KRmVsaXggQWR1IEFnZ3JleSwyMzMyNDU2MDY4NjYsMTgsMzYsbG9zZSxNZWdhLTMsMSxwYWlkLDU0LA0KTWlzcGFoICAgQWZ1YSwyMzM1NzMxNDc3MjEsNzUsMzUsbG9zZSxNZWdhLTQsMSxwYWlkLDUwLDk1DQpIYXJyaXNvbiBHeWFtZmkgS3JhaWdlciwyMzM1NTc2MzIyMDQsNTMsLGxvc2UsTWVnYS0xLDEscGFpZCwsDQo=","doc.csv")
# print(c)



def deleteobject(objname):

    try:
        s3_client.delete_object(BUCKET_NAME, 'Ghamro/'+objname)
        resp={
            'message':'Document has been deleted successfully',
            'code':200
        }
        
        return resp
    except Exception as ex:
        return("error occurred.", ex)

        