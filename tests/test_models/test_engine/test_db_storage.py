#!/usr/bin/python3
"""Test Suite for db storage"""
import unittest
from unittest.mock import patch
from models.base_model import Base
from models.engine.db_storage import DBStorage
from os import getenv


class TestDBStorage(unittest.TestCase):
    """Test Suite for DB Storage"""

    @classmethod
    def setUpClass(cls):
        """Before all the tests"""
        cls.user = getenv('VIT_MYSQL_USER')
        cls.password = getenv('VIT_MYSQL_USER')
        cls.host = getenv('VIT_MYSQL_USER')
        cls.db = getenv('VIT_MYSQL_USER')
        cls.storage = DBStorage();

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
