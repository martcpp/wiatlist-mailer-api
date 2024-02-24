from django.test import TestCase
from rest_framework.test import APIClient
from unittest.mock import patch
from .models import WaitlistEntry
from .serializers import WaitlistEntrySerializer
from .mailer import send_email

class WaitlistEntryViewTest(TestCase):

    def setUp(self):
        self.client = APIClient()

    @patch('yourapp.views.send_email')  # Mock the send_email function
    def test_waitlist_entry_creation_with_email(self, mock_send_email):
        # Mock the send_email function to avoid actual email sending during testing
        mock_send_email.return_value = None  # You can customize this as needed

        data = {'email': 'test@example.com', 'name': 'John Doe'}
        response = self.client.post('/api/v1/waitlist/', data, format='json')

        self.assertEqual(response.status_code, 201)

        # Check that the send_email function was called with the expected arguments
        mock_send_email.assert_called_once_with('Thank you for joining the waitlist!', '...', 'test@example.com', 'John Doe')

        # Check that a WaitlistEntry was created with the correct data
        waitlist_entry = WaitlistEntry.objects.get(email='test@example.com')
        self.assertEqual(waitlist_entry.name, 'John Doe')

    def test_waitlist_entry_creation_without_email(self):
        data = {'name': 'John Doe'}  # No email provided
        response = self.client.post('/api/v1/waitlist/', data, format='json')

        self.assertEqual(response.status_code, 201)

        # Check that the send_email function was not called
        with patch('yourapp.views.send_email') as mock_send_email:
            self.assertEqual(mock_send_email.called, False)

        # Check that a WaitlistEntry was created with the correct data
        waitlist_entry = WaitlistEntry.objects.get(name='John Doe')
        self.assertIsNone(waitlist_entry.email)  # Email should be None or empty depending on your model

