from django.db import models

# Create your models here.
class PyhackEvent(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    hold_dateime = models.DateTimeField()


class PyhackParticipant(models.Model):
    event = models.ForeignKey(PyhackEvent, on_delete=models.CASCADE)
    username = models.CharField(max_length=255)
