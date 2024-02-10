#!/usr/bin/python3
''' review unittes modules '''
import unittest
import os
from datetime import datetime
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    ''' unittest cases for review class '''
    def test_None(self):
        test_review = Review()
        self.assertNotIn(None, test_review.__dict__.values())

    def test_type(self):
        self.assertEqual(Review, type(Review()))
        self.assertEqual(str, type(Review().id))
        self.assertEqual(datetime, type(Review().created_at))
        self.assertEqual(datetime, type(Review().updated_at))
        self.assertEqual(str, type(Review.place_id))
        self.assertEqual(str, type(Review.user_id))
        self.assertEqual(str, type(Review.text))

    def test_unique_instance(self):
        test1 = Review()
        test2 = Review()
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
        test_review = Review()
        update1 = test_review.updated_at
        test_review.save()
        update2 = test_review.updated_at
        self.assertNotEqual(update1, update2)

    def test_str(self):
        test_review = Review()
        self.assertIn("[Review]", str(test_review))
        self.assertIn(str(test_review.__dict__), str(test_review))

    def test_to_dict(self):
        test_review = Review()
        test1 = test_review.created_at.isoformat()
        test2 = test_review.updated_at.isoformat()
        self.assertEqual(test_review.to_dict()['id'], test_review.id)
        self.assertEqual(test_review.to_dict()['created_at'], test1)
        self.assertEqual(test_review.to_dict()['updated_at'], test2)
        self.assertEqual(test_review.to_dict()['__class__'], 'Review')


if __name__ == "__main__":
    unittest.main()
