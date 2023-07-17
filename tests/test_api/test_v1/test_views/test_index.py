#!/usr/bin/python3
"""
Test suite for vitrine api index
"""
import unittest
import requests
from os import getenv


class TestViewsIndex(unittest.TestCase):
    """Test api index"""

    @classmethod
    def setUpClass(cls):
        """Before all tests"""
        cls.base_url = "http://{}:{}/api/v1".format(
            getenv("VIT_API_HOST", "0.0.0.0"), getenv("VIT_API_PORT", "5000")
        )
        brand_data = {
            "handle": "tesdleIndex",
            "name": "Tesdle",
            "email": "tesdle@test.com",
            "password": "tesdle123",
        }

        # call api to store the new user
        response = requests.post(
            "{}/brands".format(cls.base_url), json=brand_data
        )
        cls.token = response.json()["token"]

    def test_statistics(self):
        """Check if metrics endpoint returns the correct response"""
        response = requests.get(
            f"{self.base_url}/metrics", auth=(self.token, "")
        )
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)
        for value in response.json().values():
            self.assertIsInstance(value, int)
