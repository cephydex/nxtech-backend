from routes.admin.graphql_service import *




def transform_data(data):
    
   
    transformed_data = {'unique_data': [], 'duplicate_count': data['duplicate_count']}

    # Create dictionaries to map names to IDs
    title_mapping = {}
    bank_mapping ={}
    role_mapping = {}
    nationality_mapping = {}
    payment_method_mapping ={}
    
    # Extract and map title names to IDs
    for item in data['unique_data']:
      
        title_name = item['title']
        if title_name not in title_mapping:
            variables = {"name": title_name}
          
            title_data = getIdsFromTitle(variables)
            
            if title_data and 'title_id' in title_data:
        
                title_id = title_data['title_id'][0]['id'] if len(title_data['title_id'])>0 else  None
                title_mapping[title_name] = title_id


    for item in data['unique_data']:
      
        bank_name = item['bank_name']
        if bank_name not in bank_mapping:
            variables = {"name": bank_name}
          
            bank_data = getIdsFromBankName(variables)
            
            if bank_data and 'bank_id' in bank_data:
        
                bank_id = bank_data['bank_id'][0]['id'] if len(bank_data['bank_id'])>0 else  None
                bank_mapping[bank_name] = bank_id

    
    for item in data['unique_data']:
      
        payment_method = item['payment_method']
       
        if payment_method not in payment_method_mapping:
            variables = {"code": payment_method}
          
            payment_method_data = getPaymentMethodFromCode(variables)
           
            
            if payment_method_data and 'payment_method_id' in payment_method_data:
        
                payment_method_id = payment_method_data['payment_method_id'][0]['id'] if len(payment_method_data['payment_method_id'])>0 else  None
                
                payment_method_mapping[payment_method] = payment_method_id

                
    
    
    # Extract and map role names to IDs
    for item in data['unique_data']:
        role_name = item['role']
        if role_name not in role_mapping:
            variables = {"role": role_name}
            role_data = getIdsFromRole(variables)
            if role_data and 'role_id' in role_data:
                role_id = role_data['role_id'][0]['id'] if len(role_data['role_id'])>0 else  None
                role_mapping[role_name] = role_id

    # Extract and map nationality names to IDs
    for item in data['unique_data']:
        nationality_name = item['nationality']
        if nationality_name not in nationality_mapping:
            variables = {"nationality": nationality_name}
            nationality_data = getIdsFromNationality(variables)
            if nationality_data and 'nationality_id' in nationality_data:
                nationality_id = nationality_data['nationality_id'][0]['id'] if len(nationality_data['nationality_id'])>0 else  None
                nationality_mapping[nationality_name] = nationality_id

    # Transform the data by replacing names with IDs
    for item in data['unique_data']:
        title_name = item['title']
        role_name = item['role']
        nationality_name = item['nationality']
        bank_name= item['bank_name']
        payment_method_code=item['payment_method']
       

        transformed_item = item.copy()
        transformed_item['title_id'] = title_mapping.get(title_name)
        transformed_item['role_id'] = role_mapping.get(role_name)
        transformed_item['nationality'] = nationality_mapping.get(nationality_name)
        transformed_item['bank_id'] = bank_mapping.get(bank_name)
        transformed_item['payment_method']=payment_method_mapping.get(payment_method_code)

        # Remove the original name fields if you want
        transformed_item.pop('title', None)
        transformed_item.pop('role', None)
        # transformed_item.pop('nationality', None)

        transformed_data['unique_data'].append(transformed_item)
        

    return transformed_data