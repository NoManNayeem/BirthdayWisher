from rest_framework import generics
from .models import Customer
from .serializers import CustomerSerializer

class CustomerRegistrationView(generics.CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
