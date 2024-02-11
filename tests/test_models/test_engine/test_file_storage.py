#!/usr/bin/python3
''' FileStorage unittest '''
import unittest
import models
import os
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User


class TestFileStorage(unittest.TestCase):
    ''' unittest FileStorage class definition '''
    def test_types(self):
        self.assertEqual(FileStorage, type(FileStorage()))
        self.assertEqual(FileStorage, type(models.storage))
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))
        self.assertEqual(dict, type(models.storage.all()))

    def test_None(self):
        with self.assertRaises(TypeError):
            FileStorage(None)
        with self.assertRaises(TypeError):
            models.storage.all(None)
        with self.assertRaises(AttributeError):
            models.storage.new(None)
        with self.assertRaises(TypeError):
            models.storage.save(None)
        with self.assertRaises(TypeError):
            models.storage.reload(None)

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
        FileStorage._FileStorage__objects = {}

    def test_new(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)
        test_m = BaseModel()
        test_s = State()
        test_c = City()
        test_a = Amenity()
        test_p = Place()
        test_r = Review()
        test_u = User()
        models.storage.new(test_m)
        models.storage.new(test_s)
        models.storage.new(test_c)
        models.storage.new(test_a)
        models.storage.new(test_p)
        models.storage.new(test_r)
        models.storage.new(test_u)
        self.assertIn("BaseModel." + test_m.id, models.storage.all().keys())
        self.assertIn(test_m, models.storage.all().values())
        self.assertIn("State." + test_s.id, models.storage.all().keys())
        self.assertIn(test_s, models.storage.all().values())
        self.assertIn("City." + test_c.id, models.storage.all().keys())
        self.assertIn(test_c, models.storage.all().values())
        self.assertIn("Amenity." + test_a.id, models.storage.all().keys())
        self.assertIn(test_a, models.storage.all().values())
        self.assertIn("Place." + test_p.id, models.storage.all().keys())
        self.assertIn(test_p, models.storage.all().values())
        self.assertIn("Review." + test_r.id, models.storage.all().keys())
        self.assertIn(test_r, models.storage.all().values())
        self.assertIn("User." + test_u.id, models.storage.all().keys())
        self.assertIn(test_u, models.storage.all().values())

    def test_save(self):
        test_m = BaseModel()
        test_s = State()
        test_c = City()
        test_a = Amenity()
        test_p = Place()
        test_r = Review()
        test_u = User()
        models.storage.new(test_m)
        models.storage.new(test_s)
        models.storage.new(test_c)
        models.storage.new(test_a)
        models.storage.new(test_p)
        models.storage.new(test_r)
        models.storage.new(test_u)
        models.storage.save()
        file_text = ""
        with open("file.json", "r") as file:
            file_text = file.read()
            self.assertIn("BaseModel." + test_m.id, file_text)
            self.assertIn("State." + test_s.id, file_text)
            self.assertIn("City." + test_c.id, file_text)
            self.assertIn("Amenity." + test_a.id, file_text)
            self.assertIn("Place." + test_p.id, file_text)
            self.assertIn("Review." + test_r.id, file_text)
            self.assertIn("User." + test_u.id, file_text)

    def test_reload(self):
        test_m = BaseModel()
        test_s = State()
        test_c = City()
        test_a = Amenity()
        test_p = Place()
        test_r = Review()
        test_u = User()
        models.storage.new(test_m)
        models.storage.new(test_s)
        models.storage.new(test_c)
        models.storage.new(test_a)
        models.storage.new(test_p)
        models.storage.new(test_r)
        models.storage.new(test_u)
        models.storage.save()
        models.storage.reload()
        object_file = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + test_m.id, object_file)
        self.assertIn("State." + test_s.id, object_file)
        self.assertIn("City." + test_c.id, object_file)
        self.assertIn("Amenity." + test_a.id, object_file)
        self.assertIn("Place." + test_p.id, object_file)
        self.assertIn("Review." + test_r.id, object_file)
        self.assertIn("User." + test_u.id, object_file)


if __name__ == "__main__":
    unittest.main()
