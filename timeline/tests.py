import unittest
from django.test import TestCase, Client

# Create your tests here.


class TextObjectTest(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_details(self):
        response = self.client.get('/timeline/2/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['timeline']), 1)
