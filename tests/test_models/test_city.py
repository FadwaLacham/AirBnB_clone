#!/usr/bin/python3
''' city unittes modules '''
import unittest
import os
from datetime import datetime
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    ''' unittest cases for state class '''
    def test_None(self):
        test_city = City()
        self.assertNotIn(None, test_city.__dict__.values())

    def test_type(self):
        self.assertEqual(City, type(City()))
        self.assertEqual(str, type(City().id))
        self.assertEqual(datetime, type(City().created_at))
        self.assertEqual(datetime, type(City().updated_at))
        self.assertEqual(str, type(City.state_id))
        self.assertEqual(str, type(City.name))

    def test_unique_instance(self):
        test1 = City()
        test2 = City()
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
        test_city = City()
        update1 = test_city.updated_at
        test_city.save()
        update2 = test_city.updated_at
        self.assertNotEqual(update1, update2)

    def test_str(self):
        test_city = City()
        self.assertIn("[City]", str(test_city))
        self.assertIn(str(test_city.__dict__), str(test_city))

    def test_to_dict(self):
        test_city = City()
        test1 = test_city.created_at.isoformat()
        test2 = test_city.updated_at.isoformat()
        self.assertEqual(test_city.to_dict()['id'], test_city.id)
        self.assertEqual(test_city.to_dict()['created_at'], test1)
        self.assertEqual(test_city.to_dict()['updated_at'], test2)
        self.assertEqual(test_city.to_dict()['__class__'], 'City')


if __name__ == "__main__":
    unittest.main()
