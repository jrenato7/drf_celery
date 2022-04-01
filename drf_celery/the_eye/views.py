from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def store_event(request):
    """
    Receive the event data and pushes to the queue to be processed later.
    """
    import pprint
    pprint.pprint(request.data)

    return Response({"success": True})
