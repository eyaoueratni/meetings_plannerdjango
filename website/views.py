from django.shortcuts import render
from meetings.models import Meetings
# Create your views here.
 
def home_view(request):
    context={'nbre_meeting': Meetings.objects.count()}
    return render(request, "website/home.html" ,context=context)

def about_view(request):
    return render(request ,"website/about.html")

