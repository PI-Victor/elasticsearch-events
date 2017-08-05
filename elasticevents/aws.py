import boto3


class ResourceClient():
    def __init__(self, resource, access_key, secret_key):
        self.resource = resource
        self.token = access_key
        self.secret = secret_key

    def new_client(self):
        client = boto3.client(
                self.resource,
                aws_access_key_id=self.access_key,
                aws_secret_access_key=self.secret_key,
        )
        self.client = client

def apply_cf_template(access_key, secret_key, cf_template):
    cf_client = ResourceClient(
        resource='cloudformation',
        access_key=access_key,
        secret_key=secret_key,
    )
    with open(cf_template, 'r') as template:
        cf_client.validate_template(
            response = cf_client.validate_template(TemplateBody=template.read())
        )

def connect(access_key, secret_key, cf_template, lambda_zip):
    apply_cf_template(access_key, secret_key, cf_template)
