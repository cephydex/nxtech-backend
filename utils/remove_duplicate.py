def remove_duplicates(data):
    unique_items = {}
    removed_duplicates = []
    result = []

    for item in data:
        email = item['email']
        phone = item['phone']
        national_id =item['national_id']

        # Check if either email or phone is already in the dictionary
        if email in unique_items or phone in unique_items or national_id in unique_items:
            # If duplicate, add it to the removed_duplicates list
            removed_duplicates.append(item)
            continue

        unique_items[email] = item
        unique_items[phone] = item
        unique_items[national_id]=item
        result.append(item)

    return result, removed_duplicates
