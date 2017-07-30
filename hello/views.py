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

from .models import Greeting, PlainTextParser, Transactionstatus

# Create your views here.
def index(request):
    times = int(os.environ.get('TIMES',3))
    return HttpResponse('Hello! ' * times)


def waiterapp(request):
    latestStatus = Transactionstatus.objects.latest(when)
    return HttpResponse(latestStatus)
    # return HttpResponse('<meta http-equiv="refresh" content="0; URL=\'waiterapp://\'" />')

@api_view(['POST'])
@parser_classes((PlainTextParser,))
def postTransactionstatus(request):
    if request.method == 'POST':
        print(request.data);
        transactionstatus = Transactionstatus();
        transactionstatus.status = request.data;
        transactionstatus.save();
    
    return HttpResponse(status=200)
        


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})