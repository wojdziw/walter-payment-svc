from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.parsers import JSONParser
import requests
import os

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes


from django.http import HttpResponse

from rest_framework.response import Response

from .models import Greeting, PlainTextParser, TransactionStatus

# Create your views here.
def index(request):
    times = int(os.environ.get('TIMES',3))
    return HttpResponse('Hello! ' * times)


def waiterapp(request):
    times = int(os.environ.get('TIMES',3))
    return HttpResponse('Hello! ' * times)
    # return HttpResponse('<meta http-equiv="refresh" content="0; URL=\'waiterapp://\'" />')

@api_view(['POST'])
@parser_classes((PlainTextParser,))
def postTransactionStatus(request):
    if request.method == 'POST':
        print(request.data);
        transactionStatus = TransactionStatus();
        transactionStatus.status = request.data;
        transactionStatus.save();
    
    return HttpResponse(status=200)
        


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})