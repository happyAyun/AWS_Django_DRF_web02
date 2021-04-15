from django.urls import path
from . import api

urlpatterns = [
    path('', api.CommunicationList, name="todos"),
    path('detail/<str:pk>/', api.CommunicationDetail, name="detail"),
    path('create/', api.CommunicationCreate, name="create"),
    path('update/<str:pk>/', api.CommunicationUpdate, name='update'),
    path('delete/<str:pk>/', api.CommunicationDelete, name='delete'),
]
