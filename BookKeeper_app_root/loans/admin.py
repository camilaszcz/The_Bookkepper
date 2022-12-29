from django.contrib import admin
from .models import BookInstance

# Register your models here.

class BooksInstanceInline(admin.TabularInline):
    """Defines format of inline book instance insertion (used in BookAdmin)"""
    model = BookInstance

admin.site.register(BookInstance)

class BookInstanceAdmin(admin.ModelAdmin):
    """Administration object for BookInstance models.
    Defines:
     - fields to be displayed in list view (list_display)
     - filters that will be displayed in sidebar (list_filter)
     - grouping of fields into sections (fieldsets)
    """
    list_display = ('booktitle', 'borrower', 'due_back')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('booktitle', 'borrower')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )