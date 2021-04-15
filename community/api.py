from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Communication, Communication_Comment
from .modelsdto import CommunicationSerializer, Communication_CommentSerializer


@api_view(['GET'])
def CommunicationList(request):
    communications = Communication.objects.all()
    serializer = CommunicationSerializer(communications, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def CommunicationDetail(request, pk):
    communication = Communication.objects.get(communication_id=pk)
    serializer = CommunicationSerializer(communication, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def CommunicationCreate(request):
    serializer = CommunicationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['PUT'])
def CommunicationUpdate(request, pk):
    communication = Communication.objects.get(communication_id=pk)
    serializer = CommunicationSerializer(instance=communication, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def CommunicationDelete(request, pk):
    communication = Communication.objects.get(communication_id=pk)
    communication.delete()
    return Response('Deleted')
