import os
from shutil import make_archive
from base64 import b64encode

def archive_lambda_folder():
    project_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    lambda_folder = '{}/{}'.format(project_dir, 'lambda')
    # NOTE: this should have some error handling, but we skip it for now.
    return make_archive('elasticevents', 'zip', lambda_folder)

def base64_encode_zip(zip_file_path):
    with open(zip_file_path, encoding='latin-1') as zip_file:
        # NOTE: super hackish, but some python lib in boto3 uses latin-1
        # and this prevents a clean base64 encoding.
        # NOTE: also a downside is the large size this turns out to have.
        encoded = b64encode(bytes(zip_file.read(), 'utf-8'))
    return encoded