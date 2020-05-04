from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, throttle_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle

from rest_framework.decorators import api_view, schema
from rest_framework.schemas import AutoSchema
from rest_framework.generics import \
    CreateAPIView, \
    ListAPIView, \
    RetrieveAPIView, \
    UpdateAPIView, \
    DestroyAPIView, \
    ListCreateAPIView, \
    RetrieveUpdateDestroyAPIView, \
    RetrieveDestroyAPIView, \
    RetrieveUpdateAPIView


from apis.learnviews.models import Room
from apis.learnviews.serializers import RoomSerializer


class RoomCreateView(CreateAPIView):
    serializer_class = RoomSerializer
    
class RoomListView(ListAPIView):
    serializer_class = RoomSerializer
    def get_queryset(self):
        return Room.objects.all()

class RoomRetrieveView(RetrieveAPIView):
    print('inside here')
    serializer_class = RoomSerializer
    lookup_field = 'pk'
    # lookup_url_kwarg = 'title'
    queryset = Room.objects.all()

class RoomUpdateView(UpdateAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()
    lookup_field = 'pk'

class RoomDestroyView(DestroyAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()

class RoomListCreateView(ListCreateAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()


class RoomRetrieveUpdateView(RetrieveUpdateAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()


class RoomRetrieveDestroyView(RetrieveDestroyAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()




class RoomRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()



class CustomThrottleUser(UserRateThrottle):
    rate = '40/day'

class CustomThrottleAnonymous(AnonRateThrottle):
    rate = '20/day'

class RoomView(APIView):
    throttle_classes = [CustomThrottleUser, CustomThrottleAnonymous]
    permission_classes = [AllowAny]
    
    def get(self, request, format=None):
        rooms = Room.objects.all()
        context = {
            'rooms': list(rooms)
        }
        print(context)
        return Response(context)
    
    def post(self, *args, **kwargs):
        print(args[0])
        request = args[0]
        print(dir(request))
        print('hereree')
        print(request.data)
        print(self.request.data)
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(request.data)
            return Response({'data': 'data'})

        return Response({'error': 'error'})



@api_view(['GET', 'POST'])
def room(request):
    if request.method == 'GET':
        serializer = RoomSerializer()
        return Response(data=serializer.data)
    elif request.method == 'POST':
        serializer = RoomSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            print('ok')
            return Response(data=serializer.data)
        print('not saved')
        return Response(data=serializer.data)


@api_view(['GET'])
def room_list(request):
    rooms = Room.objects.all()
    serialize = RoomSerializer(rooms, many=True)
    print(type(rooms), rooms)
    print(dir(Response))
    return Response(data=serialize.data)

@api_view(['GET', 'POST'])
def room_update(request):
    id = request.data['id']
    room = Room.objects.filter(id=id)[0]
    serializer = RoomSerializer(instance=room)
    if request.method=='POST':
        # room.title = request.data['title']
        # room.price = request.data['price']
        # room.availability = request.data['availability']
        serializer = RoomSerializer(data=request.data, instance=room)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    return Response(data=serializer.data)
    


@api_view(['GET'])
@schema(AutoSchema())
def schema_view(request):
    return Response({"message": "Hello for today! See you tomorrow!"})


from apis.learnviews.serializers import CommentSerializer, Comment

@api_view(['GET', 'POST', 'PATCH', 'PUT'])
def comment_view(request):
    if request.method=='GET':
        comment = CommentSerializer(data=request.data)
        return Response(comment.initial_data)
    elif request.method=='POST':
        comment = CommentSerializer(data=request.data)
        if comment.is_valid():
            comment.save()
        return Response(comment.data)
