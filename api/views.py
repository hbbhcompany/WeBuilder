from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MessageSerializer, CardSerializer

from .models import Message,Card
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List of message':'/message/message-list/',
		'Detail View of message':'/message/message-detail/<str:pk>/',
		'Create of message':'/message/message-create/',
		'Update of message':'/message/message-update/<str:pk>/',
		'Delete of message':'/message/message-delete/<str:pk>/',
		'-------------------':'-------------------------------',
		'List of workers': '/card/card-list/',
		'Detail View of workers': '/card/card-detail/<str:pk>/'
		}

	return Response(api_urls)

@api_view(['GET'])
def messageList(request):
	messages = Message.objects.all().order_by('-id')
	serializer = MessageSerializer(messages, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def messageDetail(request, pk):
	messages = Message.objects.get(id=pk)
	serializer = MessageSerializer(messages, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def messageCreate(request):
	serializer = MessageSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def messagekUpdate(request, pk):
	message = Message.objects.get(id=pk)
	serializer = MessageSerializer(instance=message, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def messagekDelete(request, pk):
	message = Message.objects.get(id=pk)
	message.delete()

	return Response('Item succsesfully delete!')


# Cards Views
@api_view(['GET'])
def cardList(request):
	cards = Card.objects.all().order_by('-id')
	serializer = CardSerializer(cards, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def cardDetail(request, pk):
	cards = Card.objects.get(id=pk)
	serializer = CardSerializer(cards, many=False)
	return Response(serializer.data)


