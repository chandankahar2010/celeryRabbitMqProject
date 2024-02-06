from django.shortcuts import render
from celeryRabbitMqApp.tasks import consumerItem
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse,HttpResponse
import json
import pika
from celeryRabbitMqApp.models import Items
from celeryRabbitMqApp.config import *
# Create your views here.

@csrf_exempt
def producer(request):
    if request.method == 'POST':
        jsonData = request.body
        parchedData = json.loads(jsonData)
        item = parchedData.get('item')
        status = 'Pending'

        # inserting items
        Items.objects.create(item=item,status=status)
        # retreving id of item
        idOfItem = Items.objects.filter(item=item,status=status).values('id')
        id = idOfItem[0]['id']

        consumerItem.apply_async((item,id),exchange=exchangeName, routing_key=routingKey)
    
        response = {}
        response["status_code"] = "202"
        return JsonResponse(response,safe=False)

def getAllItems(request):
    if request.method == 'GET':
        allItems =  list(Items.objects.all().values())
        response = {}
        response["itemList"] = allItems
        return JsonResponse(response,safe=False)
