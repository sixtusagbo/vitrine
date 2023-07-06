#!/usr/bin/python3
"""Test Suite for DetailPoint model"""
import unittest
from models.brand import Brand
from models.base_model import BaseModel
from models.detail_point import DetailPoint
from models import storage


class TestDetailPoint(unittest.TestCase):
    """Test DetailPoint model"""

    def setUp(self):
        """Before each test"""
        self.brand = Brand()

        self.brand.name = "Some Brand"
        self.brand.handle = "some_brand"
        self.brand.email = "somebrand@example.com"
        self.brand.password = "password"

        self.point1 = DetailPoint(content="some content 1",
                                  brand_id=self.brand.id)
        self.point2 = DetailPoint(content="some content 2",
                                  brand_id=self.brand.id)

        self.brand.save()
        self.point1.save()
        self.point2.save()
        storage.reload()

    def tearDown(self):
        """After each test"""
        storage.close()

    def test_module_docstring(self):
        """check for docstring"""
        self.assertIsNotNone(DetailPoint.__doc__)

    def test_detail_point_inherits_base_model(self):
        """check for inheritance"""
        self.assertIsInstance(self.point1, BaseModel)
        self.assertIsInstance(self.point2, BaseModel)

    def test_brand_model_fields(self):
        """Check for fields"""
        self.assertEqual(self.point1.content, "some content 1")
        self.assertEqual(self.point2.content, "some content 2")
