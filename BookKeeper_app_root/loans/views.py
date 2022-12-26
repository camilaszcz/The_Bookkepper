from django.shortcuts import render, get_object_or_404
from .models import  Book, BookInstance
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime
from django.contrib.auth.decorators import login_required, permission_required
from my_library.forms import RenewBookForm
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.contrib.auth.mixins import PermissionRequiredMixin

# Create your views here.
class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    """Generic class-based view listing books on loan to current user."""
    model = BookInstance
    template_name = 'my_library/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')


# Added as part of challenge!

class LoanedBooksAllListView(PermissionRequiredMixin, generic.ListView):
    """Generic class-based view listing all books on loan. Only visible to users with can_mark_returned permission."""
    model = BookInstance
    permission_required = 'my_library.can_mark_returned'
    template_name = 'my_library/bookinstance_list_borrowed_all.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(status__exact='o').order_by('due_back')

    def renew_book_librarian(request, pk):
        """View function for renewing a specific BookInstance by librarian."""
        book_instance = get_object_or_404(BookInstance, pk=pk)

        # If this is a POST request then process the Form data
        if request.method == 'POST':

            # Create a form instance and populate it with data from the request (binding):
            form = RenewBookForm(request.POST)

            # Check if the form is valid:
            if form.is_valid():
                # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
                book_instance.due_back = form.cleaned_data['renewal_date']
                book_instance.save()

                # redirect to a new URL:
                return HttpResponseRedirect(reverse('all-borrowed'))

        # If this is a GET (or any other method) create the default form
        else:
            proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=6)
            form = RenewBookForm(initial={'renewal_date': proposed_renewal_date})

        context = {
            'form': form,
            'book_instance': book_instance,
        }

        return render(request, 'my_library/book_renew_librarian.html', context)