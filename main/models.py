from django.db import models
from advanced_queries.model import BaseModel


# Create your models here.


class Author(BaseModel):
    name = models.CharField(max_length=55, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True, unique=True)
    biography = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        db_table = 'author'
        verbose_name_plural = 'Author'

    def __str__(self):
        return f"Author {self.name}" or f"Author {self.email}"


class AuthorDetails(BaseModel):
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE)
    birth_date = models.DateTimeField(blank=True, null=True)
    nationality = models.CharField(max_length=55, blank=True, null=True)

    class Meta:
        db_table = 'author_details'
        verbose_name_plural = 'Author Details'

    def __str__(self):
        return str(self.author_id)


class Article(BaseModel):
    title = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField(max_length=1000, blank=True, null=True)
    author_id = models.ForeignKey(Author, blank=True, null=True, on_delete=models.CASCADE)
    publication_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return self.title


class Book(BaseModel):
    book_title = models.CharField(max_length=55, blank=True)
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_date = models.DateTimeField(null=True, blank=True)
    ISBN = models.CharField(max_length=255, blank=True, null=True)
    genre = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(max_length=1000, blank=True, null=True)

    class Meta:
        db_table = 'book'
        verbose_name_plural = 'Books'

    def __str__(self):
        return self.book_title


class BookReferenced(BaseModel):
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)

    class Meta:
        db_table = 'book_referenced'
        verbose_name_plural = 'Books Referenced'

    def __str__(self):
        return self.article_id + ' : ' + self.book_id


class Library(BaseModel):
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity_available = models.IntegerField(default='0', blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    shelf_number = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'library'
        verbose_name_plural = 'Libraries'

    def __str__(self):
        return f"{self.book_id} - Quantity: {self.quantity_available}"
