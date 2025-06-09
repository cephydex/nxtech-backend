import base64
import csv
from io import StringIO

def extract_csv_from_base64(base64_string):
    try:
        # Decoding the Base64 string to obtain file content
        file_content = base64.b64decode(base64_string).decode('utf-8')

        # Reading CSV content from the decoded file content
        csv_data = []
        csv_reader = csv.DictReader(StringIO(file_content))
        for row in csv_reader:
            csv_data.append(row)

        return csv_data
    except Exception as e:
        return f"Error: {str(e)}"


