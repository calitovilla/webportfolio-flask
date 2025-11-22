"""Tests for the Flask Portfolio Web Application server."""

import unittest
from server import app

class FlaskAppTestCase(unittest.TestCase):
    """Application tests for Flask Portfolio Web Application."""
    def setUp(self):
        """Set up the test environment."""
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        """Test the home page route."""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<!DOCTYPE html>', response.data)

    def test_page_valid(self):
        """Test the route for valid subpages."""
        response = self.app.get('/about')
        self.assertEqual(response.status_code, 200)

    def test_page_not_found(self):
        """Test the route for non-existent subpages."""
        response = self.app.get('/nonexistentpage')
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'Page not found', response.data)

    def test_thankyou_page(self):
        """Test the thank you page route."""
        response = self.app.get('/thankyou?email=test@example.com')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Thank you', response.data)

    def test_submit_form_valid(self):
        """Test the route for submitting the form."""
        response = self.app.post('/submit_form', data={'email': 'test@example.com'})
        self.assertEqual(response.status_code, 302)
        self.assertIn('/thankyou?email=test@example.com', response.location)
        

    def test_submit_form_missing_email(self):
        """Test the response when submitting without an email."""
        response = self.app.post('/submit_form', data={})
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'Missing required field: email', response.data)

if __name__ == '__main__':
    unittest.main()
