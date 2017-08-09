import click

from elasticevents import aws
from elasticevents.utils import archive_lambda_folder, base64_encode_zip


def validate_parameters(ctx, param, value):
    if value == '':
        raise click.BadParameter('Parameter is mandatory and can not be empty')

@click.command()
@click.option(
    '--access-key',
    default='',
    callback=validate_parameters,
    help='Token to be used for connecting to AWS resources.',
)
@click.option(
    '--secret-key',
    default='',
    callback=validate_parameters,
    help='Secret to be used for connecting to AWS resources.',
)
@click.option(
    '--cf-template',
    default='',
    callback=validate_parameters,
    type=click.Path(),
    help='Full path to a CloudFormation template.',
)
def deploy_resources(access_key, secret_key, cf_template):
    aws.connect(access_key, secret_key, cf_template)

if __name__ == '__main__':
    path_zip_file = archive_lambda_folder()
    base64_encode_zip(path_zip_file)
    deploy_resources()
