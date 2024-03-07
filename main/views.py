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

        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)

        if serializer is None:
            result_error['error'] = serializer.errors
            return Response(result_error)

        result['data'] = serializer.data

        return Response(result)

    def post(self, request, format=None, *args, **kwargs):
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

        serializer = AuthorSerializer(data=request.data)

        if serializer is None:
            result_error['error'] = serializer.errors
            return Response(result_error)

        result['data'] = serializer.data

        return Response(result)


class AuthorDetailsAPIView(APIView):

    def get_object(self, id):
        try:
            return AuthorDetails.objects.get(author_id__id=id)
        except AuthorDetails.DoesNotExist:
            raise Http404

    def get(self, request, id, *args, **kwargs):
        
        result = {
                "message": "Success",
                "status":  HTTP_200_OK,
                "data":    []
        }

        author = self.get_object(id)
        serializer = AuthorDetailsSerializer(author)
        result['data'] = serializer.data
        return Response(result)

    def post(self, request, id, *args, **kwargs):
        
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

        author_instance = self.get_object(id)
        serializer = AuthorDetailsSerializer(author_instance, data=request.data)

        if serializer.is_valid():
            serializer.save()
            result['data'] = serializer.data
            return Response(result)

        result_error['errors'] = serializer.errors
        return Response(result_error)

    def delete(self, id):
        author_instance = self.get_object(id)
        author_instance.delete()
        result = {
                "message": "Author deleted ",
                "status":  HTTP_204_NO_CONTENT
        }
        return Response(result)


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

        result = {
                "message": "Author deleted ",
                "status":  HTTP_204_NO_CONTENT
        }
        return Response(result)
