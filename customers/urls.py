from django.urls import path, include
from customers.views import CustomerRegistrationView

urlpatterns = [
    path('api/customer/register/', CustomerRegistrationView.as_view(), name='customer-register'),
]
