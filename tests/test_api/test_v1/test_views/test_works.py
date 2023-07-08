#!/usr/bin/python3
"""
Test suite for vitrine api work endpoints
"""
import unittest
import requests
from os import getenv
from models.brand import Brand
from datetime import datetime


class TestViewsWorks(unittest.TestCase):
    """Test api work endpoints"""

    @classmethod
    def setUpClass(cls):
        """Before all tests"""
        cls.base_url = "http://{}:{}/api/v1".format(
            getenv("VIT_API_HOST", "0.0.0.0"),
            getenv("VIT_API_PORT", "5000"))
        cls.acmes = Brand(name="Acme Corporations", handle="acmecorps",
                          email="info@acmecorps.com", password="acmes@123")
        cls.acmes.save()

    def test_works(self):
        """Check if works endpoint returns the correct response"""
        response = requests.get(f"{self.base_url}/brands/acmecorps/works")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_create_work(self):
        """Check if work is created"""
        work_data = {
            "title": "Acmes Project M",
            "image_url": "https://acmecorps.com/static/images/project-m"
        }
        response = requests.post(f"{self.base_url}/brands/acmecorps/works",
                                 json=work_data)
        data = response.json()
        self.assertEqual(response.status_code, 201)
        self.assertIsInstance(data, dict)
        self.assertEqual(data["title"], work_data["title"])
        self.assertEqual(data["image_url"], work_data["image_url"])
        self.assertEqual(data["brand_id"], self.acmes.id)
