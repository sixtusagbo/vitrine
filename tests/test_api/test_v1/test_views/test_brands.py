#!/usr/bin/python3
"""
Test suite for vitrine api brand endpoints
"""
import unittest
import requests
from os import getenv
from models.brand import Brand
from datetime import datetime


class TestViewsBrands(unittest.TestCase):
    """Test api brand endpoints"""
    base_url = "http://{}:{}/api/v1".format(getenv("VIT_API_HOST", "0.0.0.0"),
                                            getenv("VIT_API_PORT", "5000"))

    def test_brands(self):
        """Check if brands endpoint returns the correct response"""
        response = requests.get(f"{self.base_url}/brands")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_brand(self):
        """Check if brand endpoint returns the correct response"""
        acme = Brand(name="Acme Corporation", handle="acmecorp",
                     email="info@acmecorp.com", password="acme@123")
        acme.save()
        response = requests.get(f"{self.base_url}/brands/acmecorp")
        data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, dict)
        self.assertEqual(data["name"], acme.name)
        self.assertEqual(data["handle"], acme.handle)
        self.assertEqual(data["email"], acme.email)

    def test_create_brand(self):
        """Check if brand is created"""
        brand_data = {
            "name": "Test Brand",
            "handle": "te" + datetime.now().strftime("%Y%m.%f"),
            "email": "info@testbrand.com",
            "password": "password"
        }
        response = requests.post(f"{self.base_url}/brands", json=brand_data)
        data = response.json()
        self.assertEqual(response.status_code, 201)
        self.assertIsInstance(data, dict)
        self.assertEqual(data["name"], brand_data["name"])
        self.assertEqual(data["email"], brand_data["email"])
        self.assertEqual(data["handle"], brand_data["handle"])
