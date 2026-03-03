import unittest
from app import app

class TestFlatCMS(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_status_code(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_page_not_found(self):
        response = self.app.get('/pagina-que-no-existe-123')
        self.assertEqual(response.status_code, 404)

    def test_static_css_exists(self):
        response = self.app.get('/static/style.css')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()