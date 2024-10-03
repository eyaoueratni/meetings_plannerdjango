from . import views 
from django.urls import path
from meetings.views import detail,detail_room
urlpatterns = [
    path('meetings', views.meetings_list_view ,name='meetings'),
    path('detail/<int:id>/', detail, name='detail'),  # Meeting 
    path('rooms', views.rooms_list_view ,name='rooms'),
    path('detail_room/<int:id>/', detail_room, name='detail_room'),  # Meeting detail
]
