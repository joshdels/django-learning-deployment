from django.contrib import admin
from .models import Book, Review

from .models import Book

class ReviewInline(admin.TabularInline):
    model = Review

class BookAdmin(admin.ModelAdmin):
    '''This will control the django admin site what to show only'''
    inlines = [
        ReviewInline,
    ]
    list_display = ("title",  "author", "price",)

admin.site.register(Book, BookAdmin)


