from django.http import HttpResponse
from django.http.response import Http404
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT
from rest_framework.views import APIView

from .models import Author, AuthorDetails, Article, Book, BookReferenced, Library
from .serializers import AuthorSerializer, AuthorDetailsSerializer, ArticlesSerializer, BookSerializer, BookReferencedSerializer, LibrarySerializer


# Create your views here.

def home(request):
    return HttpResponse('This is Home')


class AuthorViewAPI(APIView):

    def get(self, request, *args, **kwargs):
        result = {
                "message": "Success",
                "status":  HTTP_200_OK,
                "data":    [],
        }

        result_error = {
                "message": "Errors",
                "status":  HTTP_400_BAD_REQUEST,
                "error":   [],
        }

        authors = Author.objects.first()
        serializer = AuthorSerializer(authors, many=False).data

        if serializer is None:
            result_error['error'] = serializer.errors
            return Response(result_error)

        result['data'] = serializer

        return Response(result)


class AuthorDetailsAPIView(APIView):

    def get_object(self, slug):
        try:
            return Author.objects.get(name=slug)
        except Author.DoesNotExist:
            raise Http404

    def get(self, slug):
        result = {
                "message": "Success",
                "status":  HTTP_200_OK,
                "data":    []
        }
        author = self.get_object(slug)
        serializer = AuthorDetailsSerializer(author)
        result['data'] = serializer.data
        return Response(result)

    def post(self, request, slug):
        result = {
                "message": "Successfully created a new author",
                "status":  HTTP_200_OK,
                "data":    []
        }

        result_error = {
                "message": "Author create failed",
                "status":  HTTP_400_BAD_REQUEST,
                "errors":  []
        }

        author_instance = self.get_object(slug)
        serializer = AuthorDetailsSerializer(author_instance, data=request.data)

        if serializer.is_valid():
            serializer.save()
            result['data'] = serializer.data
            return Response(result)

        result_error['errors'] = serializer.errors
        return Response(result_error)

    def delete(self, slug):
        author_instance = self.get_object(slug)
        author_instance.delete()
        return Response(status=HTTP_204_NO_CONTENT)


class ArticlesDetailsAPIView(APIView):
    def get_object(self, pk):
        try:
            return Article.objects.get(id=pk)
        except Article.DoesNotExist:
            raise Http404

    def get(self, pk):
        result = {
                "message": "Success",
                "status":  HTTP_200_OK,
                "data":    []
        }
        author = self.get_object(pk)
        serializer = ArticlesSerializer(author)
        result['data'] = serializer.data
        return Response(result)

    def post(self, request, pk):
        result = {
                "message": "Successfully created a new author",
                "status":  HTTP_200_OK,
                "data":    []
        }

        result_error = {
                "message": "Author create failed",
                "status":  HTTP_400_BAD_REQUEST,
                "errors":  []
        }

        articles_instance = self.get_object(pk)
        serializer = ArticlesSerializer(articles_instance, data=request.data)

        if serializer.is_valid():
            serializer.save()
            result['data'] = serializer.data
            return Response(result)

        result_error['errors'] = serializer.errors
        return Response(result_error)

    def delete(self, pk):
        article_instance = self.get_object(pk)
        article_instance.delete()

        return Response(status=HTTP_204_NO_CONTENT)
