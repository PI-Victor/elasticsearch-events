import boto3

import uuid

from .utils import archive_lambda_folder, base64_encode_zip


class ResourceClient():
    '''ResourceClient

    Is used as a client base class for all AWS resources.
    '''
    def __init__(self, resource, access_key, secret_key):
        self.resource = resource
        self.access_key = access_key
        self.secret_key = secret_key
        self._region_name = 'eu-central-1'
        self.client = boto3.client(
                self.resource,
                aws_access_key_id=self.access_key,
                region_name=self._region_name,
                aws_secret_access_key=self.secret_key,
        )


def apply_cf_template(access_key, secret_key, cf_template):
    cf_instance = ResourceClient(
        resource='cloudformation',
        access_key=access_key,
        secret_key=secret_key,
    )
    with open(cf_template, 'r') as template:
        # NOTE: this will throw a resource exception and return a response,
        # we leave this as is for now.
        cf_instance.client.validate_template(
            TemplateBody=template.read()
        )
        # create a new stack with a unique name to keep them from clashing.
        stack_name = 'elastic-{}'.format(uuid.uuid1())
        # NOTE: we rewind the cloudformation template file after validation so
        # that we can create a new stack without having to reopen it.
        template.seek(0)
        # NOTE: as as the observation above at validation.
        cf_instance.client.create_stack(
            StackName=stack_name,
            TemplateBody=template.read(),
        )

def deploy(access_key, secret_key, cf_template):
    apply_cf_template(access_key, secret_key, cf_template)
    update_lambda_function(access_key, secret_key)

def delete(access_key, secret_key, cf_stack_name):
    cf_instance = ResourceClient(
        resource='cloudformation',
        access_key=access_key,
        secret_key=secret_key,
    )
    cf_instance.client.delete_stack(
        StackName=cf_stack_name,
    )

def update_lambda_function(access_key, secret_key):
    lambda_zip_file_path = archive_lambda_folder()
    b64encoded_zip = base64_encode_zip(lambda_zip_file_path)
    lambda_instance = ResourceClient(
        resource='lambda',
        access_key=access_key,
        secret_key=secret_key,
    )
    response = lambda_instance.client.update_function_code(
        FunctionName = 'elasticevents',
        ZipFile=b64encoded_zip,
    )

def trigger_s3_resource(access_key, secret_key):
    lambda_client = ResourceClient(
        resource='s3',
        access_key=access_key,
        secret_key=secret_key,
    )
