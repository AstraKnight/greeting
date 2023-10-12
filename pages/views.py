#from django.shortcuts import render

# We use the built-in HttpResponse method instead:
from django.http import HttpResponse

# Create your views here.
def home_page_view(request):
    return HttpResponse("Hi guys! What's up?")
