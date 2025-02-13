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
    if request.method == 'POST':
        data = request.data
        serializer = PersonSerializer(data = data, many= True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    if request.method == 'PUT':
        data = request.data
        person = Person.objects.get(id = data['id'])
        serializer = PersonSerializer(person, data, partial = False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    if request.method == 'PATCH':
        data = request.data
        person = Person.objects.get(id = data['id']) 
        serializer = PersonSerializer(person, data, partial = True) #Only diff between PUT and PATCH is Partial
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    else:
        data = request.data
        person = Person.objects.get(id=data['id'])
        person.delete()
        return Response(f"Record with id:{data['id']} deleted successfully" )