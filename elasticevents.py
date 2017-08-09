import click

from elasticevents import aws


@click.group()
def cli():
    pass

@cli.command()
@click.option(
    '--access-key',
    default='',
    help='Token to be used for connecting to AWS resources.',
)
@click.option(
    '--secret-key',
    default='',
    help='Secret to be used for connecting to AWS resources.',
)
@click.option(
    '--cf-template',
    default='',
    type=click.Path(),
    help='Full path to a CloudFormation template.',
)
def deploy(access_key, secret_key, cf_template):
    aws.deploy(access_key, secret_key, cf_template)

@cli.command()
@click.option(
    '--access-key',
    default='',
    help='Token to be used for connecting to AWS resources.',
)
@click.option(
    '--secret-key',
    default='',
    help='Secret to be used for connecting to AWS resources.',
)
def trigger(access_key, secret_key):
    aws.trigger_s3_resource(access_key, secret_key)

@cli.command()
@click.option(
    '--access-key',
    default='',
    help='Token to be used for connecting to AWS resources.',
)
@click.option(
    '--secret-key',
    default='',
    help='Secret to be used for connecting to AWS resources.',
)
@click.option(
    '--cf-stack',
    default='',
    type=click.Path(),
    help='The name of the CloudFormation stack that you want to delete',
)
def delete(access_key, secret_key, cf_stack):
    aws.delete(access_key, secret_key, cf_stack)

if __name__ == '__main__':
    cli()
