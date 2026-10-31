import os
import unittest
from unittest.mock import patch
import app as m

class TestFeedback(unittest.TestCase):
    def setUp(self):
        m._attempts.clear()
        m.app.testing=True
        self.client=m.app.test_client()
        self.payload={k:v[0] for k,v in m.FIELDS.items()}
    def test_closed_by_default(self):
        with patch.dict(os.environ,{},clear=True):
            self.assertFalse(m.configured())
            self.assertEqual(self.client.post("/v1/feedback",json=self.payload,headers={"Origin":m.ORIGIN}).status_code,503)
    def test_cors_origin(self):
        self.assertEqual(self.client.post("/v1/feedback",json=self.payload,headers={"Origin":"https://evil.example"}).status_code,403)
    def test_rejects_private_fields(self):
        self.assertTrue(m.valid_answers(self.payload))
        self.assertFalse(m.valid_answers({**self.payload,"child_name":"Private"}))
        self.assertFalse(m.valid_answers({**self.payload,"topic":"<script>"}))
    def test_inconsistent_answers(self):
        flags={"CCEV_PUBLIC_COLLECTION_ENABLED":"1","CCEV_PRIVACY_READY":"1","CCEV_AGGREGATE_STORAGE_APPROVED":"1","CCEV_CONTROLLER_CONTACT":"research","CCEV_NOTICE_VERSION":"v1","CCEV_METRICS_DATABASE_URL":"postgres://fake"}
        with patch.dict(os.environ,flags,clear=True):
            self.assertEqual(self.client.post("/v1/feedback",json={**self.payload,"tried":"no","clarity":"very_clear"},headers={"Origin":m.ORIGIN}).status_code,400)
    def test_local_limiter(self):
        for i in range(6):self.assertFalse(m.limited("test-peer",1+i))
        self.assertTrue(m.limited("test-peer",9))
        self.assertFalse(m.limited("test-peer",3608))
    def test_health(self):
        self.assertEqual(self.client.get("/healthz").status_code,200)
