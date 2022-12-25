# Create your models here.
from django.db import models
from django.urls import reverse  # To generate URLS by reversing URL patterns
from datetime import date
from django.contrib.auth.models import User  # Required to assign User as a borrower

# How to make status and language a dropdown menu?
# Include texchoice field
# Unless blank=False is set on the field along with a default then a label containing "---------" will be rendered with the select box. To override this behavior, add a tuple to choices containing None; e.g. (None, 'Your String For Display'). Alternatively, you can use an empty string instead of None where this makes sense - such as on a CharField.

    
# STATUS_CHOICES = [
#         ( 'O' , 'On_loan'),
#         ( 'A', 'Available'),
#         ( 'R', 'Reserved'),
#         ( 'C', 'Currently_reading'),
#         ( 'N', 'Next_in_line'),
#         ( 'D', 'Done_reading')
# ]

# class Status(models.Model):
    
#         status = models.CharField(max_length=50,
#         choices= STATUS_CHOICES,
#         default = 'Available',
#         blank= False,
#         help_text='Book availability')
        

# LANGUAGE_CHOICES = (
#         ('En','English'),
#         ('Pt','Portuguese'),
#         ('Sp','Spanish'),
#         ('He', 'Hebrew'),
#         ('It','Italian'),
#         ('Fr', 'French'),
#     )

# class Language(models.Model):

#         language = models.CharField(
#         max_length=2,
#         choices= LANGUAGE_CHOICES,
#         default='English',
#         help_text='Language')
            
        

class Author(models.Model):
    """Model representing an author."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    # class Meta:
    #     ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('author-detail', args=[str(self.name)])

    def __str__(self):
        """String for representing the Model object."""
        return '{0}, {1}'.format(self.last_name, self.first_name)
    
# Include imagefield for the book cover

class Book(models.Model):
    """Model representing a book."""
    book_cover = models.ImageField(upload_to='photos/covers/', blank=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    # language = models.ForeignKey('Language', verbose_name='LANGUAGE',on_delete=models.CASCADE)
    language = models.CharField(max_length=200)
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the book")
    pg_num = models.IntegerField()
    # status = models.ForeignKey('Status', verbose_name='STATUS',on_delete=models.CASCADE)
    status = models.CharField(max_length=200)


    
    # research verbose name
    # move status class to top
    
    
    # class Meta:
    #     """A metaclass is a class whose instances are classes. 
    #     Just as an ordinary class defines the behavior of certain objects, 
    #     a metaclass defines the behavior of certain classes and their instances."""
    #     ordering = ['title', 'author']

    def get_absolute_url(self):
        """Returns the url to access a particular book instance."""
        return reverse('book-detail', args=[str(self.name)])

    def __str__(self):
        """String for representing the Model object."""
        return self.title

class BookInstance(models.Model):
    booktitle = models.ForeignKey('Book', on_delete=models.CASCADE)
    due_back = models.DateField(null=True, blank=True)
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=200)

    @property
    def is_overdue(self):
        """Determines if the book is overdue based on due date and current date."""
        return bool(self.due_back and date.today() > self.due_back)
    
    # class Meta:
    #     ordering = ['due_back']
    #     permissions = (("can_mark_returned", "Set book as returned"),)

    def __str__(self):
        """String for representing the Model object."""
        return '({0})'.format(self.booktitle)


   


