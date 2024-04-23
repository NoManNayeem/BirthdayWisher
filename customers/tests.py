from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Customer

class CustomerRegistrationViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_customer_registration(self):
        # Define the data to be sent in the request
        data = {
            'name': 'Test Customer',
            'email': 'test@example.com',
            "birthday": "2024-04-23"
        }

        # Send a POST request to the registration endpoint
        url = reverse('customer-register')
        response = self.client.post(url, data)

        # Check if the request was successful (HTTP 201 Created)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Check if a new Customer object was created in the database
        self.assertTrue(Customer.objects.filter(name=data['name']).exists())
        self.assertEqual(response.data['name'], data['name'])
        self.assertEqual(response.data['email'], data['email'])
        
