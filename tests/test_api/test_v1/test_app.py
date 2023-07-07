#!/usr/bin/python3
"""
Test suite for vitrine api
"""
import unittest
import requests
from os import getenv
from models import storage


class TestApp(unittest.TestCase):
    """Test api"""
    base_url = "http://{}:{}/api/v1".format(getenv("VIT_API_HOST", "0.0.0.0"),
                                            getenv("VIT_API_PORT", "5000"))

    def test_not_found(self):
        """Check if invalid endpoint returns the correct response"""
        response = requests.get(f"{self.base_url}/mimi/invalid/endpoint")
        self.assertEqual(response.status_code, 404)
        self.assertIsInstance(response.json(), dict)
        self.assertTrue("error" in response.json())
        self.assertEqual(response.json().get("error"), "Not found")
