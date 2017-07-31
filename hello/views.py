from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.parsers import JSONParser
import requests
import os

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes


from urllib.request import urlopen, Request


from django.http import HttpResponse

from rest_framework.response import Response

from .models import PlainTextParser, Transactionstatus

# Create your views here.
def index(request):
    times = int(os.environ.get('TIMES', 3))
    return HttpResponse('Hello! ' * times)

def waiterapp(request):
    times = int(os.environ.get('TIMES', 3))
    #return HttpResponse('Hello! ' * times)
    return HttpResponse('<meta http-equiv="refresh" content="0; URL=\'waiterapp://Outcome\'" />')

def getTransactionstatus(request):
    latestStatus = Transactionstatus.objects.latest('when')
    return HttpResponse(latestStatus.status)

@api_view(['POST'])
@parser_classes((JSONParser,))
def postTransactionstatus(request):
    if request.method == 'POST':
        status = (request.data['order'])['status']
        print("The transaction status received is: " + status)
        transactionstatus = Transactionstatus();
        transactionstatus.status = status;
        transactionstatus.save();
    
    return HttpResponse(status=200)



def getPaymentUri(request):

    content = {
        "notifyUrl": "https://your.eshop.com/notify",
        "customerIp": "127.0.0.1",
        "merchantPosId": "145227",
        "description": "RTV market",
        "currencyCode": "PLN",
        "totalAmount": "21000",
        "products": [
            {
                "name": "Wireless mouse",
                "unitPrice": "15000",
                "quantity": "1"
            },
            {
                "name": "HDMI cable",
                "unitPrice": "6000",
                "quantity": "1"
            }
        ]
    }
    

    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ae03207a-b012-4745-95a0-78fb5bf40bda'
    }

    request = requests.post("https://secure.payu.com/api/v2_1/orders/", json=content, headers=headers)
    
    print (request.text)

    return HttpResponse(response_body)

