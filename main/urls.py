from django.urls import path
from .views import home, AuthorViewAPI, AuthorDetailsAPIView, ArticlesDetailsAPIView

urlpatterns = [
    path('', home),
    path('authors/', AuthorViewAPI.as_view()),
    path('author/"<slug:str>"', AuthorDetailsAPIView.as_view()),
    path('articles/"<int:pk>"', ArticlesDetailsAPIView.as_view()),
]
