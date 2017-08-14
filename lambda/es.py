import os
import json

from elasticsearch import Elasticsearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth


class ESEventsDocument():
    '''ESEventsDocument

    Contains necessary information and functionality to validate a json_payload
    before creating/inserting it in an Elasticsearch instance as a document.
    '''
    def __init__(self):
        # The following environment variables need to be added to your lambda
        # function in the AWS Console.
        self.hosts = [{
            'host': os.getenv('ES_HOSTS'),
            'port': int(os.getenv('ES_PORT')),
        }]
        self.awsauth = AWS4Auth(
            os.getenv('AWS_ACCESS_KEY'),
            os.getenv('AWS_SECRET_KEY'),
            os.getenv('AWS_REGION'),
            'es',
        )
        self.client = Elasticsearch(
            hosts=self.hosts,
            http_auth=self.awsauth,
            connection_class=RequestsHttpConnection,
        )
        self._events_mapping = {
            'properties': {
                'event': {
                    'properties': {
                        'name': {
                            'type': 'string'
                        },
                        'age': {
                            'type': 'integer'
                        }
                    }
                }
            }
        }
        self._index_name = 'elasticevents'
        self._doc_type = 'events'

    def insert_index(self):
        self.client.index(
            index=self._index_name,
            doc_type=self._doc_type,
            body=self.events_payload,
        )

    def validate_events_payload(self, events_payload):
        for (k, v) in events_payload.items():
            single_event_payload = {}
            try:
                name = string(v['name'])
                age = int(v['age'])
            except Exception as e:
                print(e)
                # We log the exception, but not raise it.
                # An invalid data type in an event shouldn't kill the program.
                continue

            single_event_payload.update({'name': name, 'age': age})
            self.events_payload.update(k, single_event_payload)


    def insert_events(self, events_payload):
        self.validate_events_payload(events_payload)
        self.create_index(events_payload)
