from rest_framework import serializers
from .models import QnA, QnA_Reply


class QnASerializer(serializers.ModelSerializer):
    class Meta:
        model = QnA
        fields = ['qna_id', 'qna_title', 'qna_content', 'qna_img', 'book_id']


class QnA_ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = QnA_Reply
        fields = ['reply_id', 'reply_content', 'qna_id']
