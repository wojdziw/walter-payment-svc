from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.parsers import JSONParser
import requests
import os
import json
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from django.http import HttpResponse
from rest_framework.response import Response
from .models import PlainTextParser, TransactionStatus
import datetime

def index(request):
    times = int(os.environ.get('TIMES', 3))
    return HttpResponse('Yello! ' * times)

def payment(request):
    return HttpResponse('<html style=" padding: 40px; font-size: 40px; font-family: \'arial\'">You can now close this tab.</html>')

def getTransactionStatus(request):
    id = request.GET.get('id')
    latestStatus = TransactionStatus.objects.get(id=id)
    if (latestStatus is None):
        return HttpResponse("")
    return HttpResponse(latestStatus.status)

@api_view(['POST'])
@parser_classes((JSONParser,))
def postTransactionStatus(request):
    if request.method == 'POST':
        print(request.data)
        status = (request.data['order'])['status']
        id = request.data['order']['products'][0]['name']
        print("The transaction status received is: " + status)
        transactionstatus = TransactionStatus()
        transactionstatus.status = status
        transactionstatus.id = id
        transactionstatus.when = datetime.datetime.now()

        transactionstatus.save()

    return HttpResponse(status=200)

def getToken():
    body = "grant_type=client_credentials&client_id=301839&client_secret=53abd5b4510abc11b6ddc8bed7241a0c"
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    request = requests.post("https://secure.snd.payu.com/pl/standard/user/oauth/authorize", data=body, headers=headers)
    jdata = json.loads(request.text)
    token = jdata['access_token']

    return token

def getPaymentUri(request):
    # PUT PAYU SPECIFICS JSON HERE
    totalAmount = request.GET.get('totalAmount')
    id = request.GET.get('id')
    token = getToken()
    print(token)
    content = {
        "notifyUrl": "http://sheltered-plateau-48256.herokuapp.com/postTransactionStatus",
        "continueUrl": "https://sheltered-plateau-48256.herokuapp.com/payment",
        "customerIp": "127.0.0.1",
        "merchantPosId": "301839",
        "description": "Menu order",
        "currencyCode": "PLN",
        "totalAmount": totalAmount,
        "products": [
            {
                "name": id,
                "unitPrice": totalAmount,
                "quantity": "1"
            }
        ],
        "payMethods": {
            "payMethod": {
                "type": "PBL",
                "value": "c"
            }
        }
    }

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + token
    }

    request = requests.post("https://secure.snd.payu.com/api/v2_1/orders/", json=content, headers=headers, allow_redirects=False)

    jdata = json.loads(request.text);
    uri = jdata['redirectUri'];

    print(uri)

    return HttpResponse(uri)

def getMenuPositions(request):
    os.path.join(os.path.dirname(os.path.dirname(__file__)),'menuPositions.json')
    with open('menuPositions.json') as json_data:
        return HttpResponse(json_data)
