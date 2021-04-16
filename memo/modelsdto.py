from rest_framework import serializers
from .models import Memo


class MemoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Memo
        fields = ['memo_id', 'memo_title', 'memo_content', 'memo_date', 'memo_img', 'user_id', 'article_id', 'book_id']


