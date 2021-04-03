from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
	path('message/message-list/', views.messageList, name="message-list"),
	path('message/message-detail/<str:pk>/', views.messageDetail, name="message-detail"),
	path('message/message-create/', views.messageCreate, name="message-create"),

	path('message/message-update/<str:pk>/', views.messagekUpdate, name="message-update"),
	path('message/message-delete/<str:pk>/', views.messagekDelete, name="message-delete"),

	path('card/card-list/', views.cardList, name="card-list"),
	path('card/card-detail/<str:pk>/', views.cardDetail, name="card-detail"),

]
