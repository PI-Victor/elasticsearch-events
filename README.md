#### Elastic-Events

Elastic-Events is a tool that stores and validates events from a AWS defined
resource to a AWS elastic search instance.  

#### Installing
create a virtualenv with python3

```
virtualenv -p python3 .venv
source .venv/bin/activate
python3 setup.py install
```

##### Deploying

```
python3 elasticevents.py deploy --secret-key AWS_SECRET_KEY --access-key AWS_ACCESS_KEY --template ./cf-template
```

#### Deleting
In your CloudFormation dashboard, get the cloudformation stack name and pass it
to the cli, in order to delete it.

```
python3 elasticevents.py delete --secret-key AWS_SECRET_KEY --access-key AWS_ACCESS_KEY --stack MY_DEPLOYED_STACK_NAME
```

#### Uploading
The lambda function created from the template deploy is a dummy, that's because
of the difficulty of referencing it in the cloudformation template as a base64
encoded zip file.
In order to upload the lambda file contained in the [lambda folder](./lambda)
you need to upload it manually.
(Unfortunately, because of the large zipfile, this usually times out. The best
  alternative to this would be uploading it to an s3 bucket)
```
python3 elasticevents.py upload --secret-key AWS_SECRET_KEY --access-key AWS_ACCESS_KEY
```

#### Triggering
To trigger an event and have lambda push to your elastic search instance

```
python3 trigger --secret-key AWS_SECRET_KEY --access-key AWS_ACCESS_KEY --bucket AWS_BUCKET_NAME
```

#### Lambda + Elasticsearch domain
In order to make lambda aware of your AWS Elasticsearch domain connection
details, you need to export these env variables:
```
ES_HOSTS
ES_PORT
AWS_ACCESS_KEY
AWS_SECRET_KEY
AWS_REGION
```
