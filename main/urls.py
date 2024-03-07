from django.urls import path
from .views import home, AuthorViewAPI, AuthorDetailsAPIView, ArticlesDetailsAPIView

urlpatterns = [
    path('', home),
    path('api/authors/', AuthorViewAPI.as_view()),
    path('api/author/create/<int:id>', AuthorDetailsAPIView.as_view()),
    path('api/articles/<int:pk>', ArticlesDetailsAPIView.as_view()),
]
