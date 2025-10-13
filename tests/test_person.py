import unittest
import sys
import os

# Agregar el directorio src al path para importar
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

try:
    from person import Person
except ImportError as e:
    print(f"❌ ERROR: No se pudo importar Person desde src/person.py")
    print(f"Detalles: {e}")
    sys.exit(1)


class TestPerson(unittest.TestCase):
    """Tests para la clase Person"""
    
    def test_person_existe(self):
        """Verifica que la clase Person existe"""
        self.assertTrue(hasattr(Person, '__init__'), 
                       "La clase Person debe tener un constructor __init__")
    
    def test_person_tiene_str(self):
        """Verifica que Person implementa __str__"""
        self.assertTrue(hasattr(Person, '__str__'),
                       "La clase Person debe implementar el método __str__")
    
    def test_nombres_minusculas(self):
        """Verifica capitalización con nombres en minúsculas"""
        p = Person("juan", "perez")
        resultado = str(p)
        self.assertEqual(resultado, "Juan Perez", 
                        f"Esperado 'Juan Perez', pero obtuve '{resultado}'")
    
    def test_nombres_mayusculas(self):
        """Verifica que funciona con nombres en mayúsculas"""
        p = Person("MARIA", "LOPEZ")
        resultado = str(p)
        self.assertEqual(resultado, "Maria Lopez",
                        f"Esperado 'Maria Lopez', pero obtuve '{resultado}'")
    
    def test_nombres_mixtos(self):
        """Verifica nombres con capitalización mixta"""
        p = Person("cArLoS", "gOnZaLeZ")
        resultado = str(p)
        self.assertEqual(resultado, "Carlos Gonzalez",
                        f"Esperado 'Carlos Gonzalez', pero obtuve '{resultado}'")
    
    def test_nombres_con_espacios(self):
        """Verifica que maneja nombres compuestos"""
        p = Person("juan carlos", "de la cruz")
        resultado = str(p)
        self.assertEqual(resultado, "Juan Carlos De La Cruz",
                        f"Esperado 'Juan Carlos De La Cruz', pero obtuve '{resultado}'")
    
    def test_atributos_existen(self):
        """Verifica que los atributos first_name y last_name existen"""
        p = Person("ana", "martinez")
        self.assertTrue(hasattr(p, 'first_name'),
                       "La clase Person debe tener el atributo 'first_name'")
        self.assertTrue(hasattr(p, 'last_name'),
                       "La clase Person debe tener el atributo 'last_name'")
    
    def test_atributos_correctos(self):
        """Verifica que los atributos se asignan correctamente"""
        p = Person("pedro", "sanchez")
        self.assertEqual(p.first_name, "pedro",
                        "El atributo first_name no se asignó correctamente")
        self.assertEqual(p.last_name, "sanchez",
                        "El atributo last_name no se asignó correctamente")


if __name__ == '__main__':
    # Configurar el runner de tests para obtener información detallada
    runner = unittest.TextTestRunner(verbosity=2)
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPerson)
    result = runner.run(suite)
    
    # Salir con código de error si hay fallos
    sys.exit(0 if result.wasSuccessful() else 1)