#!/usr/bin/python3
"""Test Suite for db storage"""
from os import getenv
import unittest
from unittest.mock import patch
from models.base_model import Base
from models.engine.db_storage import DBStorage
from models.brand import Brand


class TestDBStorage(unittest.TestCase):
    """Test Suite for DB Storage"""

    @classmethod
    def setUpClass(cls):
        """Before all the tests"""
        cls.user = getenv('VIT_MYSQL_USER')
        cls.password = getenv('VIT_MYSQL_USER')
        cls.host = getenv('VIT_MYSQL_USER')
        cls.db = getenv('VIT_MYSQL_USER')
        cls.storage = DBStorage()

    @classmethod
    def tearDownClass(cls):
        """Close session after all the tests"""
        cls.storage.close()

    def setUp(self):
        """Reload db session before each test"""
        self.storage.reload()

    def tearDown(self):
        """Rollback the current session and close it after each test"""
        self.storage._DBStorage__session.rollback()
        self.storage.close()

    def test_new(self):
        """Create a new object and add it to the session"""
        obj = Brand(name="SomeBrand", email="somebrand@gmail.com",
                    handle="somebrand", password="somebrandpwd")
        self.storage.new(obj)
        self.assertIn(obj, self.storage._DBStorage__session.new)

    def test_save(self):
        """Create a new object, add it to the session, and save changes"""
        obj = Brand(name="SomeBrand", email="somebrand@gmail.com",
                    handle="somebrand", password="somebrandpwd")
        self.storage.new(obj)
        self.storage.save()
        self.assertIn(obj, self.storage._DBStorage__session)
        self.assertFalse(self.storage._DBStorage__session.dirty)

    def test_delete(self):
        """
        Create a new object, add it to the session, delete it,
        and save changes
        """
        obj = Brand(name="SomeBrand", email="somebrand@gmail.com",
                    handle="somebrand", password="somebrandpwd")
        self.storage.new(obj)
        self.storage.save()
        self.storage.delete(obj)
        self.storage.save()
        self.assertNotIn(obj, self.storage._DBStorage__session)

    def test_reload(self):
        """Test if tables are created and session is reloaded"""
        with patch.object(Base.metadata, 'create_all') as mock_create_all:
            self.storage.reload()
            mock_create_all.assert_called_once_with(
                self.storage._DBStorage__engine)
        self.assertIsNotNone(self.storage._DBStorage__session)

    def test_close(self):
        """Test if db storage has close method"""
        self.assertTrue(hasattr(DBStorage, 'close'))
