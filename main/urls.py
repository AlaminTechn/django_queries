from django.urls import path
from .views import home, AuthorViewAPI

urlpatterns = [
    path('', home),
    path('authors/', AuthorViewAPI.as_view()),
]
