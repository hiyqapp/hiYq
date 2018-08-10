from django.contrib import admin
from .models import Messenger, Message

admin.site.register(Messenger)
admin.site.register(Message)