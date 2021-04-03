from django.contrib import admin

# Register your models here.

from .models import Message, Card

admin.site.register(Message)
admin.site.register(Card)