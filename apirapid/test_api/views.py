from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

from . import models
from test_api.serializers import TestApiSerializer



# Create your views here.
@csrf_exempt
def all(request):
    if request.method == 'GET':
        data = models.TestApi.objects.all()
        data_serialized = TestApiSerializer(data,many=True)
        return JsonResponse(data_serialized.data,safe=False)

@csrf_exempt
def new(request):
    if request.method == 'POST':
        print('came here')
        data = JSONParser().parse(request)
        data_serialized=TestApiSerializer(data=data)
        if data_serialized.is_valid():
            data_serialized.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)