from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PersonSerializer
from .models import Person
# Create your views here.

@api_view(['GET'])
def index(request):
    profile = {
        'name': 'Bharat',
        'age': 29,
        'Job': 'Dev'
    }
    return Response(profile)

@api_view(['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
def personView(request):
    if request.method == 'GET':
        person = Person.objects.all()
        serializer = PersonSerializer(person, many=True)
        return Response(serializer.data)
    