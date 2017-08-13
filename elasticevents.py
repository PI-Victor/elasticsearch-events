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
    '--template',
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
@click.option(
    '--bucket',
    default='',
    help='Name of the bucket that is used to trigger the lambda function.',
)
def trigger(access_key, secret_key, bucket):
    aws.trigger_s3_resource(access_key, secret_key, bucket)

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
    '--stack',
    default='',
    type=click.Path(),
    help='The name of the CloudFormation stack that you want to delete',
)
def delete(access_key, secret_key, stack):
    aws.delete(access_key, secret_key, stack)

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
def update(access_key, secret_key):
    aws.update_lambda(access_key, secret_key)

if __name__ == '__main__':
    cli()
