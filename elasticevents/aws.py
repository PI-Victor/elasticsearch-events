import boto3
import uuid


class S3BucketEvent():
    '''S3BucketEvent represents an event that is triggered once an upload to a
    S3 bucket has been done.
    '''
    def validate_event(self):
        pass


class ResourceClient():
    '''ResourceClient is used as a base class for all resources that need to
    manipulate AWS resources.
    '''
    def __init__(self, resource, access_key, secret_key):
        self.resource = resource
        self.token = access_key
        self.secret = secret_key
        self.client = boto3.client(
                self.resource,
                aws_access_key_id=self.access_key,
                aws_secret_access_key=self.secret_key,
        )


def apply_cf_template(access_key, secret_key, cf_template):
    cf_client = ResourceClient(
        resource='cloudformation',
        access_key=access_key,
        secret_key=secret_key,
    )
    with open(cf_template, 'r') as template:
        response = cf_client.validate_template(
            TemplateBody=template.read()
        )
        # create a new stack with a unique name to keep them from clashing.
        stack_name = 'elastic-{}'.format(uuid.uuid1())
        # NOTE: we rewind the cloudformation template file after validation so
        # that we can create a new stack without having to reopen it.
        template.seek(0)
        # response = cf_client.create_stack(
        #     StackName=stack_name,
        #     TemplateBody=template.read(),
        # )

def connect(access_key, secret_key, cf_template, lambda_zip):
    apply_cf_template(access_key, secret_key, cf_template)
    upload_base64_lambda()

def upload_base64_lambda(access_key, secret_key, lambda_zip):

    pass
