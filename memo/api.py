from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Memo
from .modelsdto import MemoSerializer


@api_view(['GET'])
def MemoList(request):
    memos = Memo.objects.all()
    serializer = MemoSerializer(memos, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def MemoDetail(request, pk):
    memo = Memo.objects.get(memoId=pk)
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
    memo = Memo.objects.get(memoId=pk)
    serializer = MemoSerializer(instance=memo, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def MemoDelete(request, pk):
    memo = Memo.objects.get(memoId=pk)
    memo.delete()
    return Response('Deleted')
