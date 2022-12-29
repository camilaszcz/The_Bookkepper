from django.db import models
from django.contrib.auth.models import User
from my_library.models import Book, Status
from django.urls import reverse  # To generate URLS by reversing URL patterns
from datetime import date

# Create your models here.


        
class BookInstance(models.Model):
    booktitle = models.ForeignKey(Book, on_delete=models.CASCADE)
    due_back = models.DateField(null=True, blank=True)
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.ForeignKey(Status,on_delete=models.CASCADE)

    @property
    def is_overdue(self):
        """Determines if the book is overdue based on due date and current date."""
        return bool(self.due_back and date.today() > self.due_back)
    
    class Meta:
        ordering = ['due_back']
        permissions = (("can_mark_returned", "Set book as returned"),)

    def __str__(self):
        """String for representing the Model object."""
        return '({0})'.format(self.booktitle)
