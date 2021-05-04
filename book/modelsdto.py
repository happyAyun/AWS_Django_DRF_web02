from rest_framework import serializers
from .models import Book, Book_Article, Bookmark, SignBook


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['book_id', 'book_title', 'book_content', 'book_writter', 'book_intro', 'book_like', 'book_publisher',
                  'book_img', 'book_subscribe', 'user_id']


class Book_ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book_Article
        fields = ['article_id', 'article_title', 'article_content', 'article_img', 'article_date', 'article_views',
                  'book_id']


class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = ['bookmark_id', 'user_id', 'book_id', 'article_id']


class BookProfile(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ('book_id', 'book_title', 'book_writter', 'book_intro')


class BookUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['book_id', 'book_title', 'book_content', 'book_writter', 'book_intro',
                  'book_publisher', 'book_img']

class Book_ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book_Article
        fields = ['article_id', 'article_title']


class Book_ArticleUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book_Article
        fields = ['article_id', 'article_title', 'article_content', 'article_img']


class Book_ArticleOriginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book_Article
        fields = ['article_id', 'article_title', 'book_id']


class BookmarkListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = ['bookmark_id', 'book_id', 'article_id']


class BookSignSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignBook
        fields = ['id', 'book_id', 'user_id']


class BookCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['book_id', 'book_title', 'book_writter','book_publisher']