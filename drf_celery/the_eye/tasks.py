from celery import shared_task
from .serializers import EventSerializer, PageViewSerializer, \
    PageClickSerializer, EventFormSerializer


@shared_task()
def validate_event_task(event):
    return _validate_event(event)


def _validate_event(event_data):
    serializer_event = EventSerializer(data=event_data)

    # validate event
    event_valid = serializer_event.is_valid()

    if event_valid:
        # validate payload
        payload = serializer_event.validated_data["data"]
        event_name = serializer_event.validated_data["name"]
        event_category = serializer_event.validated_data["category"]

        if event_name == "pageview" and event_category == "page interaction":
            serializer_payload = PageViewSerializer(data=payload)
        elif event_name == "cta click" and event_category == "page interaction":
            serializer_payload = PageClickSerializer(data=payload)
        elif event_name == "submit" and event_category == "form interaction":
            serializer_payload = EventFormSerializer(data=payload)
        else:
            raise Exception("Payload not found!")

        if serializer_payload.is_valid():
            # store records on DB
            event_data = serializer_event.validated_data
            event_data.pop("data")

            event = serializer_event.create(event_data)
            payload["event_id"] = event.id

            serializer_payload.create(payload)
        else:
            print(serializer_payload.errors)
            # raise Exception("Payload Invalid!")
    else:
        # raise Exception("Event Invalid!")
        print(serializer_event.errors)
