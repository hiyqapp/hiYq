from django.db import models
from account.models import Account

class Messenger(models.Model):
	sender = models.ForienKey(Account, on_delete=models.CASCADE)
	reviever = models.ForienKey(Account, on_delete=models.CASCADE)


class Message(models.Model):
	chat = models.ForienKey(Chat, on_delete=models.CASCADE)
	sent = models.DateTimeField()
	recieved = models.DateTimeField()
	text = models.TextField()
