import json

from celery import shared_task

from .serializers import EventSerializer, PageViewSerializer, \
    PageClickSerializer, EventFormSerializer
from .models import ErrorLog


class InvalidPayload(Exception):
    pass


class SerializerError(Exception):
    pass


@shared_task()
def validate_event_task(event):
    return validate_event(event)


def validate_event(event_data):
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
        elif "click" in event_name and event_category == "page interaction":
            serializer_payload = PageClickSerializer(data=payload)
        elif event_name == "submit" and event_category == "form interaction":
            serializer_payload = EventFormSerializer(data=payload)
        else:
            message = 'Payload not found!'
            log_error(event_data, message)
            raise InvalidPayload(message)

        if serializer_payload.is_valid():
            # store records on DB
            event_data = serializer_event.validated_data
            event_data.pop("data")

            event = serializer_event.create(event_data)
            payload["event_id"] = event.id

            serializer_payload.create(payload)
        else:
            message = 'Payload Invalid!'
            log_error(event_data, message, serializer_payload.errors)
            raise SerializerError(message)
    else:
        message = 'Event Invalid!'
        log_error(event_data, message, serializer_event.errors)
        raise SerializerError(message)


def log_error(event_data, message, errors=None):
    error_data = {
        'event': json.dumps(event_data),
        'errors': json.dumps(errors) if errors else None,
        'message': message
    }
    error = ErrorLog.objects.create(**error_data)
    error.save()
