#!/usr/bin/python3
"""
Test suite for vitrine api index
"""
import unittest
import requests
from os import getenv
from models import storage


class TestViewsIndex(unittest.TestCase):
    """Test api index"""
    base_url = "http://{}:{}/api/v1".format(getenv("VIT_API_HOST", "0.0.0.0"),
                                            getenv("VIT_API_PORT", "5000"))

    def test_statistics(self):
        """Check if metrics endpoint returns the correct response"""
        response = requests.get(f"{self.base_url}/metrics")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)
        for value in response.json().values():
            self.assertIsInstance(value, int)
