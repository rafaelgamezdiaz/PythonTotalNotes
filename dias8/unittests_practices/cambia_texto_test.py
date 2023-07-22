"""
 Codigo ejemplo unittest
"""
import unittest
import cambia_texto


class TestCambiaTexto(unittest.TestCase):
    """Clase de Test"""


    def test_mayusculas(self):
        palabra = "buen dia"
        resultado = cambia_texto.todo_mayusculas(palabra)
        self.assertEqual(resultado, "BUEN DIA")


if __name__ == '__main__':
    unittest.main()

