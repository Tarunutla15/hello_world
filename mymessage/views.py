from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse

def send_hello(request):
    return HttpResponse("Hello from the Django!")
