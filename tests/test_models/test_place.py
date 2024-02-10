#!/usr/bin/python3
''' Place unittes modules '''
import unittest
import os
from datetime import datetime
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    ''' unittest cases for Place class '''
    def test_None(self):
        test_place = Place()
        self.assertNotIn(None, test_place.__dict__.values())

    def test_type(self):
        self.assertEqual(Place, type(Place()))
        self.assertEqual(str, type(Place().id))
        self.assertEqual(datetime, type(Place().created_at))
        self.assertEqual(datetime, type(Place().updated_at))
        self.assertEqual(str, type(Place.city_id))
        self.assertEqual(str, type(Place.user_id))
        self.assertEqual(str, type(Place.name))
        self.assertEqual(str, type(Place.description))
        self.assertEqual(int, type(Place.number_rooms))
        self.assertEqual(int, type(Place.number_bathrooms))
        self.assertEqual(int, type(Place.price_by_night))
        self.assertEqual(float, type(Place.latitude))
        self.assertEqual(float, type(Place.longitude))
        self.assertEqual(list, type(Place.amenity_ids))

    def test_unique_instance(self):
        test1 = Place()
        test2 = Place()
        self.assertNotEqual(test1.id, test2.id)

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
        test_place = Place()
        update1 = test_place.updated_at
        test_place.save()
        update2 = test_place.updated_at
        self.assertNotEqual(update1, update2)

    def test_str(self):
        test_place = Place()
        self.assertIn("[Place]", str(test_place))
        self.assertIn(str(test_place.__dict__), str(test_place))

    def test_to_dict(self):
        test_place = Place()
        test1 = test_place.created_at.isoformat()
        test2 = test_place.updated_at.isoformat()
        self.assertEqual(test_place.to_dict()['id'], test_place.id)
        self.assertEqual(test_place.to_dict()['created_at'], test1)
        self.assertEqual(test_place.to_dict()['updated_at'], test2)
        self.assertEqual(test_place.to_dict()['__class__'], 'Place')


if __name__ == "__main__":
    unittest.main()
