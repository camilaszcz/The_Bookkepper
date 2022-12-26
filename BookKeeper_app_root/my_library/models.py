# Create your models here.
from django.db import models
from django.urls import reverse  # To generate URLS by reversing URL patterns
from datetime import date
from django.contrib.auth.models import User  # Required to assign User as a borrower

# How to make status and language a dropdown menu?
# Include texchoice field
# Unless blank=False is set on the field along with a default then a label containing "---------" will be rendered with the select box. To override this behavior, add a tuple to choices containing None; e.g. (None, 'Your String For Display'). Alternatively, you can use an empty string instead of None where this makes sense - such as on a CharField.

# Generally, it’s best to define choices inside a model class, and to define a suitably-named constant for each value:

# from django.db import models

# class Student(models.Model):
#     FRESHMAN = 'FR'
#     SOPHOMORE = 'SO'
#     JUNIOR = 'JR'
#     SENIOR = 'SR'
#     GRADUATE = 'GR'
#     YEAR_IN_SCHOOL_CHOICES = [
#         (FRESHMAN, 'Freshman'),
#         (SOPHOMORE, 'Sophomore'),
#         (JUNIOR, 'Junior'),
#         (SENIOR, 'Senior'),
#         (GRADUATE, 'Graduate'),
#     ]
#     year_in_school = models.CharField(
#         max_length=2,
#         choices=YEAR_IN_SCHOOL_CHOICES,
#         default=FRESHMAN,
#     )

#     def is_upperclass(self):
#         return self.year_in_school in {self.JUNIOR, self.SENIOR}   


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

class Author(models.Model):
    """Model representing an author."""
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    
    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('author-detail', args=[str(self.last_name, self.first_name)])

    def __str__(self):
        """String for representing the Model object."""
        return '{0}, {1}'.format(self.last_name, self.first_name)
  
        
    
# Include imagefield for the book cover

class Book(models.Model):
    """Model representing a book."""
    book_cover = models.ImageField(upload_to='media/photos/covers/')
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, related_name="books", on_delete = models.SET_NULL, null=True)
    # (Author, verbose_name="Author", on_delete=models.CASCADE)
    language = models.ForeignKey(Language, related_name='books',on_delete=models.CASCADE)
    # language = models.CharField(max_length=200)
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the book")
    pg_num = models.IntegerField()
    status = models.ForeignKey(Status, related_name='books',on_delete=models.CASCADE)

    # status = models.CharField(max_length=200)

    def get_absolute_url(self):
        """Returns the url to access a particular book instance."""
        return reverse('book-detail', args=[str(self.title)])

    def __str__(self):
        """String for representing the Model object."""
        return self.title



   


