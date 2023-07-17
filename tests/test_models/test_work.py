#!/usr/bin/python3
"""Test Suite for Work model"""
import unittest

import requests
from models.brand import Brand
from models.base_model import BaseModel
from models.work import Work
from models import storage


class TestWork(unittest.TestCase):
    """Test Work model"""

    def setUp(self):
        """Before each test"""
        self.brand = Brand()

        self.brand.name = "Some Brand"
        self.brand.handle = "some_brand"
        self.brand.email = "somebrand@example.com"
        self.brand.password = "password"

        self.work = Work(
            title="Some Brand Work",
            description="some work description",
            image_url="some_image.png",
            brand_id=self.brand.id,
        )

        self.brand.save()
        self.work.save()
        storage.reload()

    def tearDown(self):
        """After each test"""
        storage.close()

    def test_module_docstring(self):
        """check for docstring"""
        self.assertIsNotNone(Work.__doc__)

    def test_work_inherits_base_model(self):
        """check for inheritance"""
        self.assertIsInstance(self.work, BaseModel)

    def test_brand_model_fields(self):
        """Check for fields"""
        self.assertEqual(self.work.title, "Some Brand Work")
        self.assertEqual(self.work.description, "some work description")
        self.assertEqual(self.work.image_url, "some_image.png")
