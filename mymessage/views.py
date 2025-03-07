from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse

@api_view(['GET'])
def send_hello(request):
    return Response({"message": "Hello from the Django!"})
