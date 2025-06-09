
import random
import string

def generate_ip_numberString(usertype):
    if usertype=="publisher":
        random_number = ''.join(random.choices(string.digits, k=8))
        # Combine 'INS-' with the random number
        random_id = f"PUB-{random_number}"
        return random_id
    elif usertype=="member":
        random_number = ''.join(random.choices(string.digits, k=8))
        # Combine 'INS-' with the random number
        random_id = f"MEM-{random_number}"
        return random_id
    else:
        random_number = ''.join(random.choices(string.digits, k=8))
        # Combine 'INS-' with the random number
        random_id = f"RCL-{random_number}"
        return random_id


