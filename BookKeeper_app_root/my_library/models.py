# Create your models here.
from django.db import models
from django.urls import reverse  # To generate URLS by reversing URL patterns
from datetime import date
from django.contrib.auth.models import User  # Required to assign User as a borrower

# How to make status and language a dropdown menu?
# Include texchoice field

# from django_utils.choices import Choice, Choices

# class Book(models.Model):
#    class STATUS(Choices):
#        available = Choice('available', _('Available to borrow'))
#        borrowed = Choice('borrowed', _('Borrowed by someone'))
#        archived = Choice('archived', _('Archived - not available anymore'))

#    # [...]
#    status = models.CharField(
#        max_length=32,
#        choices=STATUS.choices,
#        default=STATUS.available,
#    )


class Status(models.Model):
    CHOICES = (
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
        ('c', 'Currently_reading'),
        ('n', 'Next_in_line'),
        ('d', 'Done_reading'),
    )
    
    status = models.CharField(
        max_length=1,
        choices= CHOICES,
        blank=True,
        default='a',
        help_text='Book availability')     


# Include texchoice field
class Language(models.Model):
    """Model representing a Language (e.g. English, French, Japanese, etc.)"""
    CHOICES = (
        ('En','English'),
        ('Pt','Portuguese'),
        ('Sp','Spanish'),
        ('He', 'Hebrew'),
        ('It','Italian'),
        ('Fr', 'French'),
    )
    
    language = models.CharField(
        max_length=2,
        choices= CHOICES,
        blank=True,
        default='English',
        help_text='Language')    

class Author(models.Model):
    """Model representing an author."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('author-detail', args=[str(self.name)])

    def __str__(self):
        """String for representing the Model object."""
        return '{0}, {1}'.format(self.last_name, self.first_name)
    
# Include imagefield for the book cover

class Book(models.Model):
    """Model representing a book."""
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    language = models.ManyToManyField('Language', verbose_name='language')
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the book")
    pg_num = models.IntegerField()
    status = models.ManyToManyField('Status', verbose_name='books')
    
    # research verbose name
    # move status class to top
    
    
    class Meta:
        """A metaclass is a class whose instances are classes. 
        Just as an ordinary class defines the behavior of certain objects, 
        a metaclass defines the behavior of certain classes and their instances."""
        ordering = ['title', 'author']

    def get_absolute_url(self):
        """Returns the url to access a particular book instance."""
        return reverse('book-detail', args=[str(self.name)])

    def __str__(self):
        """String for representing the Model object."""
        return self.title

class BookInstance(models.Model):
    book = models.ForeignKey('Book', on_delete=models.RESTRICT, null=True) 
    due_back = models.DateField(null=True, blank=True)
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.ManyToManyField(Status, verbose_name='bookintances')

    @property
    def is_overdue(self):
        """Determines if the book is overdue based on due date and current date."""
        return bool(self.due_back and date.today() > self.due_back)
    
    class Meta:
        ordering = ['due_back']
        permissions = (("can_mark_returned", "Set book as returned"),)

    def __str__(self):
        """String for representing the Model object."""
        return '({0})'.format(self.book.title)


   


