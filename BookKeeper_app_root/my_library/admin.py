from django.contrib import admin
from .models import Book, Status, Language



# # admin.site.register(Author)
# admin.site.register(Status)


class BookAdmin(admin.ModelAdmin):
   
    list_display = ('title', 'status', 'book_cover')
    # list_display_links = ('status', 'title')
    # list_filter = ('status',)

    # search_fields = ('title', 'author', 'language')
    # list_per_page = 20
   

admin.site.register(Book, BookAdmin)
