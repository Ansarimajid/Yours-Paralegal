from asyncio.windows_events import NULL
from django.db import models

class Quote(models.Model):

    name = models.CharField(max_length=50 )
    email = models.CharField(max_length=30 )
    phone = models.CharField(max_length=20 )
    service = models.CharField(max_length=40 )
    massege = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    state = models.CharField(max_length=40 )
    

    def __str__(self):
        return self.name
