from rest_framework.utils.encoders import JSONEncoder

from django.test import TestCase
from datetime import datetime, date, timedelta
from uuid import uuid4


class JSONEncodeTests(TestCase):

    def setUp(self):
        self.encoder = JSONEncoder()

    def test_encode_datetime(self):
        current_time = datetime.now()
        self.assertEqual(self.encoder.default(current_time), current_time.isoformat())

    def test_encode_date(self):
        current_date = date.today()
        self.assertEqual(self.encoder.default(current_date), current_date.isoformat())

    def test_encode_time(self):
        current_time = datetime.now().time()
        self.assertEqual(self.encoder.default(current_time), current_time.isoformat()[:12])

    def test_encode_timedelta(self):
        delta = timedelta(hours=1)
        self.assertEqual(self.encoder.default(delta), str(delta.total_seconds()))

    def test_encode_uuid(self):
        unique_id = uuid4()
        self.assertEqual(self.encoder.default(unique_id), str(unique_id))
