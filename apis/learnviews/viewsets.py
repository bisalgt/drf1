from rest_framework import viewsets
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.decorators import action

from apis.learnviews.models import Room
from apis.learnviews.serializers import RoomSerializer, RoomSerializerId


# we can use multiple views using viewset
class RoomViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def list(self, request):
        rooms = Room.objects.all()
        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        room = Room.objects.get(id=pk)
        serializer = RoomSerializer(room)
        return Response(serializer.data)

class RommModelViewSet(viewsets.ModelViewSet):
    serializer_class = RoomSerializer
    throttle_classes = []
    queryset = Room.objects.all()

    # adding action to include more detail action on the viewse
    # other than list, create, update, partial_update, destroy, retrieve
    @action(detail=False, methods=['GET'])
    def room_list_with_id(self, *args):
        rooms = Room.objects.all()
        serializer = RoomSerializerId(rooms, many=True)
        return Response(serializer.data)


class RommModelViewSetRouter(viewsets.ModelViewSet):
    serializer_class = RoomSerializer
    lookup_field = 'title'
    throttle_classes = []
    # 
    # queryset = Room.objects.all()

# Not using query set asks for basename not set for url names, we need to declare basename at routers for this problem
    def get_queryset(self):
        return Room.objects.all()

