from django import forms
from my_library.models import Book


class CreateBookForm(forms.ModelForm):
     class Meta:
        model = Book
        fields = '__all__'
    
    
# The new class contains a nested class: Meta
# which specifies the model that this form will be for, 
# and which fields from that model to include in this form (in this case, all of them). 