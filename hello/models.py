from django.db import models
from rest_framework.parsers import BaseParser

class Transactionstatus(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)
    id = models.CharField(max_length=100, primary_key=True)
    status = models.CharField(max_length=30)

class PlainTextParser(BaseParser):
    media_type = 'text/plain'

    def parse(self, stream, media_type=None, parser_context=None):
        return stream.read()