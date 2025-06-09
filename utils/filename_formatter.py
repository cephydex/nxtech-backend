import uuid


def formatFilename(filename):
    new_file_name= f'{uuid.uuid4().hex}-{filename}'
    return new_file_name