from django.urls import path
from . import views


urlpatterns = [
    path('loans/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path(r'loans/', views.LoanedBooksAllListView.as_view(), name='all-borrowed'),  # Added for challenge
]