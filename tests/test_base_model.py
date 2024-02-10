#!/usr/bin/python3
''' unittest for base_model '''
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    ''' Unittests to test BaseModel class '''
    def test_None(self):
        test_model = BaseModel()
        self.assertNotIn(None, test_model.__dict__.values())

    def test_type(self):
        test_model = BaseModel()
        self.assertEqual(BaseModel, type(test_model))
        self.assertEqual(str, type(test_model.id))
        self.assertEqual(datetime, type(test_model.created_at))
        self.assertEqual(datetime, type(test_model.updated_at))

    def test_unique_id_update(self):
        test_mod1 = BaseModel()
        test_mod2 = BaseModel()
        self.assertNotEqual(test_mod1.id, test_mod2.id)
        self.assertNotEqual(test_mod1.updated_at, test_mod2.updated_at)

    def test_save(self):
        test_model = BaseModel()
        update1 = test_model.updated_at
        test_model.save()
        self.assertNotEqual(update1, test_model.updated_at)

    def test_str(self):
        test_model = BaseModel()
        self.assertIn("[BaseModel]", str(test_model))
        self.assertIn(str(test_model.__dict__), str(test_model))

    def test_to_dict(self):
        test_model = BaseModel()
        test1 = test_model.created_at.isoformat()
        test2 = test_model.updated_at.isoformat()
        self.assertEqual(dict, type(test_model.to_dict()))
        self.assertEqual(test_model.to_dict()['id'], test_model.id)
        self.assertEqual(test_model.to_dict()['created_at'], test1)
        self.assertEqual(test_model.to_dict()['updated_at'], test2)
        self.assertEqual(test_model.to_dict()['__class__'], 'BaseModel')


if __name__ == "__main__":
    unittest.main()
