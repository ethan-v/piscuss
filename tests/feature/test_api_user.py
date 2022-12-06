from django.test import TestCase
from rest_framework.test import APIClient

client = APIClient()


class APIUserTest(TestCase):
    """ Test module for /api/users enpoint """

    def test_get_user_list(self):
        response = client.get('/api/users')
        self.assertEqual(200, response.status_code)