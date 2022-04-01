from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .tasks import validate_event_task


@api_view(['POST'])
def store_event(request):
    """
    Receive the event data and pushes to the queue to be processed later.
    """
    event_data = JSONParser().parse(request)

    # receive the event info and sent it to the queue
    validate_event_task.delay(event_data)

    return Response({"success": True})
