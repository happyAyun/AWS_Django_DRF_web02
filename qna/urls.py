from django.urls import path
from . import api

urlpatterns = [
    path('qna/', api.QnAList, name="QnAList"),
    path('qna/detail/<str:pk>/', api.QnADetail, name="QnADetail"),
    path('qna/create/', api.QnACreate, name="QnACreate"),
    path('qna/update/<str:pk>/', api.QnAUpdate, name='QnAUpdate'),
    path('qna/delete/<str:pk>/', api.QnADelete, name='QnADelete'),
]