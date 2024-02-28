from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
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
