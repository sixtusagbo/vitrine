#!/usr/bin/python3
"""Test Suite for Brand model"""
import unittest
from models.brand import Brand
from models import storage
from models.base_model import BaseModel


class TestBrand(unittest.TestCase):
    """Test Brand model"""

    def setUp(self):
        """Before each test"""
        self.brand = Brand()

        self.brand.name = "Some Brand"
        self.brand.handle = "some_brand"
        self.brand.email = "somebrand@example.com"
        self.brand.password = "password"

        self.brand.save()
        storage.reload()

    def tearDown(self):
        """After each test"""
        storage.close()

    def test_module_docstring(self):
        """check for docstring"""
        self.assertIsNotNone(Brand.__doc__)

    def test_brand_inherits_base_model(self):
        """check for inheritance"""
        self.assertIsInstance(self.brand, BaseModel)

    def test_brand_model_fields(self):
        """Check for fields"""
        self.assertEqual(self.brand.name, "Some Brand")
        self.assertEqual(self.brand.handle, "some_brand")
        self.assertEqual(self.brand.email, "somebrand@example.com")
        self.assertIsNotNone(self.brand.password)
