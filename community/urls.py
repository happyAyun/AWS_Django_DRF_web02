from django.urls import path
from . import api

urlpatterns = [
    path('', api.CommunicationList, name="CommunicationList"),
    path('detail/<str:pk>/', api.CommunicationDetail, name="CommunicationDetail"),
    path('create/', api.CommunicationCreate, name="CommunicationCreate"),
    path('update/<str:pk>/', api.CommunicationUpdate, name='CommunicationUpdate'),
    path('delete/<str:pk>/', api.CommunicationDelete, name='CommunicationDelete'),
]
