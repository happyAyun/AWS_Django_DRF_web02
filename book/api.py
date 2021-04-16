from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Book, Book_Article, Bookmark
from .modelsdto import BookSerializer, Book_ArticleSerializer, BookmarkSerializer


@api_view(['GET'])
def BookList(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def BookDetail(request, pk):
    book = Book.objects.get(book_id=pk)
    serializer = BookSerializer(book, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def BookCreate(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['PUT'])
def BookUpdate(request, pk):
    book = Book.objects.get(book_id=pk)
    serializer = BookSerializer(instance=book, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)



@api_view(['GET'])
def Book_ArticleList(request):
    bookArticles = Book_Article.objects.all()
    serializer = Book_ArticleSerializer(bookArticles, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def Book_ArticleDetail(request, pk):
    bookArticle = Book_Article.objects.get(article_id=pk)
    serializer = Book_ArticleSerializer(bookArticle, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def Book_ArticleCreate(request):
    serializer = Book_ArticleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['PUT'])
def Book_ArticleUpdate(request, pk):
    bookArticle = Book_Article.objects.get(article_id=pk)
    serializer = Book_ArticleSerializer(instance=bookArticle, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)