# Create your views here.

from django.http import HttpResponse

def home(request):
    return HttpResponse("<H1> Hello, Django! </H1><BR>Welcome to Docker - Fun starts")