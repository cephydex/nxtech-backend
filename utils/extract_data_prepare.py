import csv
from python_graphql_client import GraphqlClient
from dotenv import load_dotenv
from requests.structures import CaseInsensitiveDict
import os
from typing import Dict



load_dotenv()

url:str = os.getenv('HASURA_GRAPHQL_URL')
token:str = os.getenv('HASURA_GRAPHQL_TOKEN')
headers:str = CaseInsensitiveDict()
headers["content-type"] = "application/json"
headers[os.getenv("HASURA_GRAPHQL_SECRET")] = token




def extract_data(file_like_object) -> Dict[str, list]:
    # Define the headers you want to extract
    headers = ["Composer", "Performer", "Arranger", "Lyricist", "Publisher"]

    # Create a dictionary to store data for each header
    users = {header: [] for header in headers}

    # Read the CSV file content
    reader = csv.reader(file_like_object)
    current_header = None  # Track the current header being processed
    for row in reader:
        if row and row[0] in headers:
            current_header = row[0]
        elif row and current_header and row[0] != 'Name' and any(row):  # Skip the first and empty rows
            name = row[0]
            share = row[1]
            ip_number = row[2]
            users[current_header].append({
                "name": name,
                "ip_number": ip_number,
                "share": share
            })
    return users

def get_roles_from_id(role_id):
    roles=[]
    query="""
        query MyQuery($id: uuid) {
        roles(where: {id: {_eq: $id}}) {
            id
            name
        }
        }
    """
    variables = {"id": role_id}
    client = GraphqlClient(endpoint=url, headers=headers)
    response: dict = client.execute(query=query, variables=variables)
    if response['data'] and len(response['data']['roles']) > 0:
        roles.append(response['data']['roles'][0]['name'])
    return roles



def transform_data(data):
    transformed_data = {header: [] for header in data.keys()}  # Initialize dictionary with empty lists for each header
    for key, items in data.items():
        if key in ['Lyricist', 'Composer', 'Performer', 'Arranger']:
            for item in items:
                ip_number = item['ip_number']
                query = """
                query MyQuery($ip_number: String) {
                  artistes(where: {ip_number: {_eq: $ip_number}}) {
                    stage_name
                    legal_name
                    id
                    email
                    role
                  }
                }
                """
                variables = {"ip_number": ip_number}
                client = GraphqlClient(endpoint=url, headers=headers)
                response: dict = client.execute(query=query, variables=variables)
                if 'data' in response and 'artistes' in response['data'] and response['data']['artistes']:
                    stage_name = response['data']['artistes'][0]['stage_name']
                    legal_name = response['data']['artistes'][0]['legal_name']
                    email = response['data']['artistes'][0]['email']
                    role_id = response['data']['artistes'][0]['role']
                    artiste_id = response['data']['artistes'][0]['id']
                    roles= get_roles_from_id(role_id)
                    transformed_data[key].append({
                        'legal_name': legal_name,
                        'stage_name': stage_name,
                        'ip_number': ip_number,
                        'share': item['share'],
                        'email' : email,
                        'id' : artiste_id,
                        # 'roles': ['']
                    })
                else:
                    transformed_data[key].append({
                        'legal_name': item['name'],
                        'stage_name': item['name'],
                        'ip_number': ip_number,
                        'share': item['share']
                        

                    })

        # elif key == 'Label':
        #     for item in items:
        #         ip_number = item['ip_number']
        #         query = """
        #         query MyQuery($ip_number: String) {
        #           record_labels(where: {ip_number: {_eq: $ip_number}}) {
        #             founder
        #           }
        #         }
        #         """
        #         variables = {"ip_number": ip_number}
        #         client = GraphqlClient(endpoint=url, headers=headers)
        #         response: dict = client.execute(query=query, variables=variables)
        #         if 'data' in response and 'record_labels' in response['data'] and response['data']['record_labels']:
        #             founder = response['data']['record_labels'][0]['founder']
        #             transformed_data[key].append({
        #                 'name': founder,
        #                 'ip_number': ip_number,
        #                 'share': item['share']
        #             })
        #         else:
        #             transformed_data[key].append({
        #                 'name': item['name'],
        #                 'ip_number': ip_number,
        #                 'share': item['share']
        #             })
        else:  # For other headers like Publisher
            for item in items:
                ip_number = item['ip_number']
                query = """
                query MyQuery($ip_number: String) {
                    publishers(where: {ip_number: {_eq: $ip_number}}) {
                        id
                        company {
                        name: business_name
                        email
                        
                        }
                    }
                    }

                """
                variables = {"ip_number": ip_number}
                client = GraphqlClient(endpoint=url, headers=headers)
                response: dict = client.execute(query=query, variables=variables)
                if 'data' in response and 'publishers' in response['data'] and response['data']['publishers']:
                    company_name = response['data']['publishers'][0]['company']['name']
                    email = response['data']['publishers'][0]['company']['email'],
                    publisher_id = response['data']['publishers'][0]['id']
                    transformed_data[key].append({
                        'name': company_name,
                        'ip_number': ip_number,
                        'share': item['share'],
                        'roles':['publisher'],
                        'email':email,
                        'id':publisher_id

                    })
                else:
                    transformed_data[key].append({
                        'name': item['name'],
                        'ip_number': ip_number,
                        'share': item['share'],
                        # 'roles':['publisher']
                    })

    return transformed_data



