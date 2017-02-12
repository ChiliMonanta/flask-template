import unittest
import json
import main

class TestMain(unittest.TestCase):

    def setUp(self):
        self.app = main.app.test_client()

    def test_index_implicit(self):
        resp = self.app.get('/')
        self.assertTrue(b'Yggdrasil' in resp.data)

    def test_index_explicit(self):
        resp = self.app.get('/index')
        self.assertTrue(b'Yggdrasil' in resp.data)

    def test_template(self):
        resp = self.app.get('/template/FooBar')
        self.assertTrue(b'Hello FooBar!' in resp.data)

    def test_command(self):
        resp = self.app.get('/command')
        self.assertEqual(204, resp.status_code)

    def test_status(self):
        resp = self.app.get('/status?arg1=OK')
        self.assertTrue('Content-Type: application/json' in str(resp.headers))
        self.assertEqual({"result":"OK"}, json.loads(resp.get_data(as_text=True)))