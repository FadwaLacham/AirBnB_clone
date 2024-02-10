#!/usr/bin/python3
''' stat unittes modules '''
import unittest
import os
from datetime import datetime
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    ''' unittest cases for state class '''
    def test_None(self):
        test_state = State()
        self.assertNotIn(None, test_state.__dict__.values())

    def test_type(self):
        self.assertEqual(State, type(State()))
        self.assertEqual(str, type(State().id))
        self.assertEqual(datetime, type(State().created_at))
        self.assertEqual(datetime, type(State().updated_at))
        self.assertEqual(str, type(State.name))

    def test_unique_instance(self):
        test1 = State()
        test2 = State()
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
        test_state = State()
        update1 = test_state.updated_at
        test_state.save()
        update2 = test_state.updated_at
        self.assertNotEqual(update1, update2)

    def test_str(self):
        test_state = State()
        self.assertIn("[State]", str(test_state))
        self.assertIn(str(test_state.__dict__), str(test_state))

    def test_to_dict(self):
        test_state = State()
        test1 = test_state.created_at.isoformat()
        test2 = test_state.updated_at.isoformat()
        self.assertEqual(test_state.to_dict()['id'], test_state.id)
        self.assertEqual(test_state.to_dict()['created_at'], test1)
        self.assertEqual(test_state.to_dict()['updated_at'], test2)
        self.assertEqual(test_state.to_dict()['__class__'], 'State')


if __name__ == "__main__":
    unittest.main()
