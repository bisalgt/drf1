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



from apis.learnviews.viewsets import \
    RoomViewSet, RommModelViewSet, RommModelViewSetRouter
from rest_framework.routers import DefaultRouter

from apis.learnviews import routerfile

router = DefaultRouter()
router.register('room_router', RoomViewSet, basename='room_router')
router.register('room_modelviewset', RommModelViewSet)
router.register('room_router_set', RommModelViewSetRouter, basename='room-router-set')


urlpatterns = router.urls




urlpatterns += [
    path('room_list/', RoomViewSet.as_view({'get': 'list'})),
    path('room_retrieve/<int:pk>/', RoomViewSet.as_view({'get': 'retrieve'})),
]
    

from apis.learnviews.views import comment_view

urlpatterns += [
    path('comment/', comment_view),
]


