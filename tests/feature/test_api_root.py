from django.test import TestCase
from rest_framework.test import APIClient

client = APIClient()


class APIRootTest(TestCase):
    """ Test module for Restful API """

    def test_root(self):
        response = client.get('/api/')
        self.assertEqual(200, response.status_code)