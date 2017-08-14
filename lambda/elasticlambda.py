from es import ESEventsDocument


def lambda_handler(event, context):
    _events_payload = {
    	"Event1": {
    		"name": "Lisa",
    		"age": 15
    	},
    	"Event2": {
    		"name": "Peter",
    		"age": 11
    	},
    	"Event3": {
    		"name": "Michael",
    		"age": "hundred"
    	}
    }
    es_doc = ESEventsDocument()
    es_doc.insert_events(_events_payload)
