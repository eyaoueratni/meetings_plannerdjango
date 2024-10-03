from django.shortcuts import render
from meetings.models import Meetings
from meetings.models import Room

# Create your views here.
def meetings_list_view(request):
    meetings = Meetings.objects.all()  # Get all meetings
    return render(request, 'meetings.html', {'meetings': meetings, })

def detail(request, id):
   meeting = Meetings.objects.get(pk=id)
   return render(request, "details.html", {"meeting": meeting})

def rooms_list_view(request):
    rooms = Room.objects.all()  # Get all rooms
    return render(request, 'rooms.html', {'rooms': rooms, })
def detail_room(request, id):
   room = Room.objects.get(pk=id)
   return render(request, "room_details.html", {"room": room})