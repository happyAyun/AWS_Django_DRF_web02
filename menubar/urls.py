from django.urls import path
from . import api

urlpatterns = [
    path('memo/', api.MemoList, name="MemoList"),
    path('memo/detail/<str:pk>/', api.MemoDetail, name="MemoDetail"),
    path('memo/create/', api.MemoCreate, name="MemoCreate"),
    path('memo/update/<str:pk>/', api.MemoUpdate, name='MemoUpdate'),
    path('memo/delete/<str:pk>/', api.MemoDelete, name='MemoDelete'),

    path('qna/', api.QnAList, name="QnAList"),
    path('qna/detail/<str:pk>/', api.QnADetail, name="QnADetail"),
    path('qna/create/', api.QnACreate, name="QnACreate"),
    path('qna/update/<str:pk>/', api.QnAUpdate, name='QnAUpdate'),
    path('qna/delete/<str:pk>/', api.QnADelete, name='QnADelete'),
]