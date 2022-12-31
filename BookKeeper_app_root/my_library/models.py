# Create your models here.
from django.db import models
from django.urls import reverse  # To generate URLS by reversing URL patterns
from django.contrib.auth.models import User  # Required to assign User as a borrower


STATUS_CHOICES = [
        ( 'On_loan' , 'On_loan'),
        ( 'Available', 'Available'),
        ( 'Reserved', 'Reserved'),
        ( 'Currently_reading', 'Currently_reading'),
        ( 'Next_in_line', 'Next_in_line'),
        ( 'Done_reading', 'Done_reading')
]

class Status(models.Model):
        status = models.CharField(max_length=20,
        choices= STATUS_CHOICES,
        help_text='Book availability')
        
        def __str__(self):
            return self.status 
        

LANGUAGE_CHOICES = [
        ('English','English'),
        ('Portuguese','Portuguese'),
        ('Spanish','Spanish'),
        ('Hebrew', 'Hebrew'),
        ('Italian','Italian'),
        ('French', 'French'),
    ]

class Language(models.Model):

    language = models.CharField(
    max_length=15,
    choices= LANGUAGE_CHOICES,
    help_text='Language')
            
    def __str__(self):
        return self.language        

class Book(models.Model):
    """Model representing a book."""
    book_cover = models.ImageField(upload_to= "{% static 'images/covers/' %}", null=True, blank=True)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50, default="Unkown")
    language = models.ForeignKey(Language, related_name='books',on_delete=models.CASCADE)
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the book")
    pg_num = models.IntegerField()
    status = models.ForeignKey(Status, related_name='books',on_delete=models.CASCADE)
    
 
