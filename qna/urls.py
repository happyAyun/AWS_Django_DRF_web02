from django.urls import path
from . import api

urlpatterns = [
    path('', api.QnAList, name="QnAList"),
    path('detail/<str:pk>/', api.QnADetail, name="QnADetail"),
    path('create/', api.QnACreate, name="QnACreate"),
    path('update/<str:pk>/', api.QnAUpdate, name='QnAUpdate'),
    path('delete/<str:pk>/', api.QnADelete, name='QnADelete'),
]