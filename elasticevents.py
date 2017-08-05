import click

from elasticevents import aws


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
@click.option(
    '--lambda-zip',
    default='',
    callback=validate_parameters,
    type=click.Path(),
    help='Full path to a lambda-zip file.',
)
def deploy_resources(access_key, secret_key, cf_template, lambda_zip):
    aws.connect(access_key, secret_key, cf_template, lambda_zip)

if __name__ == '__main__':
    deploy_resources()
