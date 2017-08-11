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
python3 elasticevents.py deploy --secret-key AWS_SECRET_KEY --access-key AWS_ACCESS_KEY --cf-template ./cf-template
```

#### Deleting
In your CloudFormation dashboard, get the cloudformation stack name and pass it
to the cli, in order to delete it.

```
python3 elasticevents.py delete --secret-key AWS_SECRET_KEY --access-key AWS_ACCESS_KEY --cf-stack MY_DEPLOYED_STACK_NAME
```

#### Triggering
To trigger an event and have lambda push to your elastic search instance

```
python3 trigger --secret-key AWS_SECRET_KEY --access-key AWS_ACCESS_KEY --bucket AWS_BUCKET_NAME
```
