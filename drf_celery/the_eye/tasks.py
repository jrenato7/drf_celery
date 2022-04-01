from celery import shared_task
from .serializers import EventSerializer


@shared_task(queue='events')
def validate_event_task(event):
    return _validate_event(event)


def _validate_event(event_data):
    serializer_event = EventSerializer(data=event_data)
    event_valid = serializer_event.is_valid()

    if event_valid:
        # validate payload
        payload = serializer_event.get_attribute('data')
        import pprint
        print(type(payload))
        pprint.pprint(payload)
