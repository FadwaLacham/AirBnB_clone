#!/usr/bin/python3
''' stat unittes modules '''
import unittest
import os
from datetime import datetime
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    ''' unittest cases for state class '''
    def test_None(self):
        test_user = User()
        self.assertNotIn(None, test_user.__dict__.values())

    def test_type(self):
        self.assertEqual(User, type(User()))
        self.assertEqual(str, type(User().id))
        self.assertEqual(datetime, type(User().created_at))
        self.assertEqual(datetime, type(User().updated_at))
        self.assertEqual(str, type(User.email))
        self.assertEqual(str, type(User.password))
        self.assertEqual(str, type(User.first_name))
        self.assertEqual(str, type(User.last_name))

    def test_unique_instance(self):
        test1 = User()
        test2 = User()
        self.assertNotEqual(test1.id, test2.id)
        self.assertNotEqual(test1.created_at, test2.created_at)
        self.assertNotEqual(test1.updated_at, test2.updated_at)

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp.json")
        except FileNotFoundError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            os.rename("tmp.json", "file.json")
        except FileNotFoundError:
            pass

    def test_save(self):
        test_user = User()
        update1 = test_user.updated_at
        test_user.save()
        update2 = test_user.updated_at
        self.assertNotEqual(update1, update2)

    def test_str(self):
        test_user = User()
        self.assertIn("[User]", str(test_user))
        self.assertIn(str(test_user.__dict__), str(test_user))

    def test_to_dict(self):
        test_user = User()
        test1 = test_user.created_at.isoformat()
        test2 = test_user.updated_at.isoformat()
        self.assertEqual(test_user.to_dict()['id'], test_user.id)
        self.assertEqual(test_user.to_dict()['created_at'], test1)
        self.assertEqual(test_user.to_dict()['updated_at'], test2)
        self.assertEqual(test_user.to_dict()['__class__'], 'User')


if __name__ == "__main__":
    unittest.main()
