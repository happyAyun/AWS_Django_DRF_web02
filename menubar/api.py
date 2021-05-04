from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Memo, QnA, QnA_Reply
from .modelsdto import MemoSerializer, QnASerializer, QnA_ReplySerializer


@api_view(['GET'])
def MemoList(request):
    memos = Memo.objects.all()
    serializer = MemoSerializer(memos, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def MemoDetail(request, pk):
    memo = Memo.objects.get(memo_id=pk)
    serializer = MemoSerializer(memo, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def MemoCreate(request):
    serializer = MemoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['PUT'])
def MemoUpdate(request, pk):
    memo = Memo.objects.get(memo_id=pk)
    serializer = MemoSerializer(instance=memo, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def MemoDelete(request, pk):
    memo = Memo.objects.get(memo_id=pk)
    memo.delete()
    return Response('Deleted')



@api_view(['GET'])
def QnAList(request):
    qnas = QnA.objects.all()
    serializer = QnASerializer(qnas, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def QnADetail(request, pk):
    qna = QnA.objects.get(qna_id=pk)
    serializer = QnASerializer(qna, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def QnACreate(request):
    serializer = QnASerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['PUT'])
def QnAUpdate(request, pk):
    qna = QnA.objects.get(qna_id=pk)
    serializer = QnASerializer(instance=qna, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def QnADelete(request, pk):
    qna = QnA.objects.get(qna_id=pk)
    qna.delete()
    return Response('Deleted')
