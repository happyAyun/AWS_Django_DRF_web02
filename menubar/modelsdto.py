from rest_framework import serializers
from .models import Memo, QnA, QnA_Reply


class MemoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Memo
        fields = ['memo_id', 'memo_title', 'memo_content', 'memo_date', 'memo_img', 'user_id', 'article_id', 'book_id']


class QnASerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = QnA
        fields = ['qna_id', 'qna_title', 'qna_content', 'qna_img', 'book_id']


class QnA_ReplySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = QnA_Reply
        fields = ['reply_id', 'reply_content', 'qna_id']
