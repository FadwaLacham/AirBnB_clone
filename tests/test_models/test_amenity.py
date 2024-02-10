#!/usr/bin/python3
''' Amenity unittes modules '''
import unittest
import os
from datetime import datetime
from models.amenity import Amenity
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    ''' unittest cases for Amenity class '''
    def test_None(self):
        test_ame = Amenity()
        self.assertNotIn(None, test_ame.__dict__.values())

    def test_type(self):
        self.assertEqual(Amenity, type(Amenity()))
        self.assertEqual(str, type(Amenity().id))
        self.assertEqual(datetime, type(Amenity().created_at))
        self.assertEqual(datetime, type(Amenity().updated_at))
        self.assertEqual(str, type(Amenity.name))

    def test_unique_instance(self):
        test1 = Amenity()
        test2 = Amenity()
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
        test_ame = Amenity()
        update1 = test_ame.updated_at
        test_ame.save()
        update2 = test_ame.updated_at
        self.assertNotEqual(update1, update2)

    def test_str(self):
        test_ame = Amenity()
        self.assertIn("[Amenity]", str(test_ame))
        self.assertIn(str(test_ame.__dict__), str(test_ame))

    def test_to_dict(self):
        test_ame = Amenity()
        test1 = test_ame.created_at.isoformat()
        test2 = test_ame.updated_at.isoformat()
        self.assertEqual(test_ame.to_dict()['id'], test_ame.id)
        self.assertEqual(test_ame.to_dict()['created_at'], test1)
        self.assertEqual(test_ame.to_dict()['updated_at'], test2)
        self.assertEqual(test_ame.to_dict()['__class__'], 'Amenity')


if __name__ == "__main__":
    unittest.main()
