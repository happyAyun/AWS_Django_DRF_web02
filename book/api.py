from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Book, Book_Article, Bookmark
from .modelsdto import BookSerializer, Book_ArticleSerializer, BookmarkSerializer, \
    BookProfile, BookUpdateSerializer, Book_ArticleListSerializer, Book_ArticleUpdateSerializer, \
    BookmarkListSerializer

@api_view(['GET'])
def BookList(request):
    print(request)
    books = Book.objects.values('book_title', 'book_writter', 'book_intro')
    print(books)
    serializer = BookProfile(books,  many=True, context={'request': request})
    return Response(serializer.data)

@api_view(['GET'])
def MyBookList(request, pk):
    books = Book.objects.get(user_id=pk)
    serializer = BookProfile(books,  many=True)
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
    serializer = BookUpdateSerializer(instance=book, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def Book_ArticleList(request, pk):
    bookArticles = Book_Article.objects.get(book_id=pk)
    serializer = Book_ArticleListSerializer(bookArticles, many=True)
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
    serializer = Book_ArticleUpdateSerializer(instance=bookArticle, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def BookmarkList(request):
    bookmarks = Bookmark.objects.all()
    serializer = BookmarkListSerializer(bookmarks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def BookmarkDetail(request, pk):
    bookmark = Bookmark.objects.get(bookmark_id=pk)
    serializer = BookmarkSerializer(bookmark, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def BookmarkCreate(request):
    serializer = BookmarkSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['PUT'])
def BookmarkUpdate(request, pk):
    bookmark = Bookmark.objects.get(bookmark_id=pk)
    serializer = BookmarkSerializer(instance=bookmark, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def BookmarkDelete(request, pk):
    bookmark = Bookmark.objects.get(bookmark_id=pk)
    bookmark.delete()
    return Response('Deleted')

@api_view(['GET'])
def Book_ArticleAllList(request):
    bookArticles = Book_Article.objects.all()
    serializer = Book_ArticleListSerializer(bookArticles, many=True)
    return Response(serializer.data)