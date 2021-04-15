from rest_framework import serializers
from .models import Communication, Communication_Comment

class CommunicationSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta:
        model = Communication
        fields = ['communication_id', 'communication_title', 'communication_content', 'communication_img', 'communication_date', 'communication_views', 'communication_category']



class Communication_CommentSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta:
        model = Communication_Comment
        fields = ['comment_id', 'comment_content', 'communication_id']
