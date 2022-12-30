from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import datetime  # for checking renewal date range.

from my_library.models import Book


class CreateBookForm(forms.ModelForm):
     class Meta:
        model = Book
        fields = '__all__'
    
    
