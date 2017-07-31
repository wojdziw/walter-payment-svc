from django.db import models
from rest_framework.parsers import BaseParser

class Transactionstatus(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)
    status = models.CharField(max_length=30)

class PlainTextParser(BaseParser):
    """
    Plain text parser.
    """
    media_type = 'text/plain'

    def parse(self, stream, media_type=None, parser_context=None):
        """
        Simply return a string representing the body of the request.
        """
        return stream.read()