import unittest
from flask import Flask
from server import app, generate_unique_string

class FlaskAPITestCase(unittest.TestCase):

    def setUp(self):
        # Create a test client
        self.app = app.test_client()
        self.app.testing = True
        self.base = "http://127.0.0.1:5000/"
        self.test_url = "https://www.google.com/"
        self.key = '0OGWoM'
        # add a URL for our testing
        self.response = self.app.post(self.base + "url", json={"url": self.test_url})

    def test_get_endpoint_returns_long_url(self):
        response = self.app.get(self.base + "url/" + self.key)
        headers = response.headers
        self.assertEqual(headers['Location'], self.test_url)


    def test_post_endpoint_creates_short_url(self):
        # Send a POST request to the API endpoint
        test_url = "https://www.example.com/"
        test_key = "STZeK2"
        test_short_url = self.base + 'url/' + test_key
        response = self.app.post(self.base + "url", json={"url": test_url})
        # Access the JSON response
        response_data = response.json
        self.assertEqual(response_data['short_url'], test_short_url)

    def test_generate_unique_string(self):
        key = generate_unique_string(self.test_url)
        self.assertEqual(key, self.key)



