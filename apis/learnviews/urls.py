from django.urls import path

from apis.learnviews.views import RoomView, room, room_list, room_update

urlpatterns = [
    path('', RoomView.as_view(), name='room_view'),
    path('room/', room, name='room'),
    path('room_list/', room_list, name='room_list'),
    path('room_update/', room_update, name='room_update'),
    
]