import unittest
from app import app

class TestFlatCMS(unittest.TestCase):

    def setUp(self):
        # Configuramos el cliente de prueba de Flask
        self.app = app.test_client()
        self.app.testing = True

    def test_home_status_code(self):
        # Verifica que el índice cargue correctamente (Código 200)
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_page_not_found(self):
        # Verifica que si buscamos una página que NO existe, devuelva un 404
        response = self.app.get('/pagina-que-no-existe-123')
        self.assertEqual(response.status_code, 404)

    def test_static_css_exists(self):
        # Verifica que el archivo CSS sea accesible
        response = self.app.get('/static/style.css')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()