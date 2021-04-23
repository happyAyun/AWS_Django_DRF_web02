from rest_framework import serializers
from .models import Memo


class MemoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Memo
        fields = ['memoId', 'memoTitle', 'memoContent', 'memoDate', 'memoImg', 'userId', 'bookId']


class MemoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Memo
        fields = ['memoId', 'memoTitle', 'memoContent', 'articleId', 'bookId', 'userId']
