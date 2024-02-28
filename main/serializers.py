from rest_framework import serializers
from .models import Author, AuthorDetails, Article, Book, BookReferenced, Library


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class AuthorDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorDetails
        fields = '__all__'


class ArticlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class BookReferencedSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookReferenced
        fields = '__all__'


class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = '__all__'
