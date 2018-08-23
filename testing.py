
from api import app
import unittest

class TestApi(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_root(self):
        req = self.app.get('/exoplanets')
        data = req.get_json()
        self.assertEqual(req.status_code, 200)
        self.assertEqual(len(data), 2)

    def test_rand(self):
        req = self.app.get('/exoplanets/rand/3')
        data = req.get_json()
        self.assertEqual(req.status_code, 200)
        self.assertEqual(len(data), 3)

    def test_exoplanets(self):
        req = self.app.get('/exoplanets/rand/3')
        rnd = req.get_json()
        for i in rnd:
          req = self.app.get('/exoplanets/id/' + i)
          data = req.get_json()
          self.assertEqual(req.status_code, 200)
          self.assertEqual(data['pl_name'].replace(' ', '_').lower(), i)

if __name__ == '__main__':
    unittest.main()

