from django.contrib import admin

from .models import Book

class BookAdmin(admin.ModelAdmin):
    '''This will control the django admin site what to show only'''
    list_display = ("title",  "author", "price",)

admin.site.register(Book, BookAdmin)
