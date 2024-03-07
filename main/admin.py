from django.contrib import admin

from .models import Author, AuthorDetails, Article, Book, BookReferenced, Library


# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    readonly_fields = ['created_at', 'updated_at',]
    list_display = ['name', 'created_at', 'updated_at']


admin.site.register(Author, AuthorAdmin)


class AuthorDetailsAdmin(admin.ModelAdmin):
    readonly_fields = ['created_at', 'updated_at']
    list_display = ['author_id', 'created_at', 'updated_at']


admin.site.register(AuthorDetails, AuthorDetailsAdmin)


class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ['created_at', 'updated_at']
    list_display = ['title', 'created_at', 'updated_at']


admin.site.register(Article, ArticleAdmin)


class BookAdmin(admin.ModelAdmin):
    readonly_fields = ['created_at', 'updated_at']
    list_display = ['book_title', 'created_at', 'updated_at']


admin.site.register(Book, BookAdmin)


class BookReferencedAdmin(admin.ModelAdmin):
    readonly_fields = ['created_at', 'updated_at']
    list_display = ['article_id', 'book_id', 'created_at', 'updated_at']


admin.site.register(BookReferenced, BookReferencedAdmin)


class LibraryAdmin(admin.ModelAdmin):
    readonly_fields = ['created_at', 'updated_at']
    list_display = ['book_id', 'quantity_available', 'location', 'shelf_number', 'created_at', 'updated_at']


admin.site.register(Library, LibraryAdmin)
