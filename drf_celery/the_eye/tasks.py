from celery import shared_task
from .serializers import EventSerializer, PageViewSerializer, \
    PageClickSerializer, AccountSubmitFormSerializer


@shared_task()
def validate_event_task(event):
    return _validate_event(event)


def _validate_event(event_data):
    serializer_event = EventSerializer(data=event_data)
    event_valid = serializer_event.is_valid()

    if event_valid:
        # validate payload
        payload = serializer_event.data["data"]
        event_name = serializer_event.data["name"]
        event_category = serializer_event.data["category"]

        if event_name == "pageview" and event_category == "page interaction":
            serializer_payload = PageViewSerializer(data=payload)
        elif event_name == "cta click" and event_category == "page interaction":
            serializer_payload = PageClickSerializer(data=payload)
        elif event_name == "submit" and event_category == "form interaction":
            serializer_payload = AccountSubmitFormSerializer(data=payload)
        else:
            raise Exception("Payload not found!")

        if serializer_payload.is_valid():
            import pprint; pprint.pprint(serializer_payload.data)
