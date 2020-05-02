from django.urls import path

from apis.learnviews.views import \
    RoomView, \
    room, \
    room_list, \
    room_update, \
    schema_view, \
    RoomCreateView, \
    RoomListView, \
    RoomRetrieveView, \
    RoomUpdateView, \
    RoomDestroyView, \
    RoomListCreateView, \
    RoomRetrieveUpdateDestroyView, \
        RoomRetrieveUpdateView, \
            RoomRetrieveDestroyView

urlpatterns = [
    path('', RoomView.as_view(), name='room_view'),
    path('room/create/', RoomCreateView.as_view(), name='room_create'),
    path('room/list/', RoomListView.as_view()),
    path('room/retrieve/<int:pk>/', RoomRetrieveView.as_view()),
    path('room/update/<int:pk>/', RoomUpdateView.as_view()),
    path('room/destroy/<int:pk>/', RoomDestroyView.as_view()),
    path('room/listcreate/', RoomListCreateView.as_view()),
    path('room/retrieveupdatedestroy/<int:pk>/', RoomRetrieveUpdateDestroyView.as_view()),
    path('room/retrieveupdate/<int:pk>/', RoomRetrieveUpdateView.as_view()),
    path('room/retrievedestroy/<int:pk>/', RoomRetrieveDestroyView.as_view()),
    path('room/', room, name='room'),
    path('room_list/', room_list, name='room_list'),
    path('room_update/', room_update, name='room_update'),
    path('schema_view/', schema_view, name='schema_view'),
    
]