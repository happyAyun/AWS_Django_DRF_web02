from django.urls import path
from . import api

urlpatterns = [
    path('', api.CommunicationList, name="CommunicationList"),
    path('detail/<str:pk>/', api.CommunicationDetail, name="CommunicationDetail"),
    path('create/', api.CommunicationCreate, name="CommunicationCreate"),
    path('update/<str:pk>/', api.CommunicationUpdate, name='CommunicationUpdate'),
    path('delete/<str:pk>/', api.CommunicationDelete, name='CommunicationDelete'),

    path('', api.CommunicationList, name="CommunicationList"),
    path('commend/create/', api.CommunicationCreate, name="CommunicationCreate"),
    path('commend/update/<str:pk>/', api.CommunicationUpdate, name='CommunicationUpdate'),
    path('commend/delete/<str:pk>/', api.CommunicationDelete, name='CommunicationDelete'),
]
