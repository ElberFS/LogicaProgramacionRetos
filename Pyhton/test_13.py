# /*
#  * EJERCICIO:
#  * Crea una función que se encargue de sumar dos números y retornar
#  * su resultado.
#  * Crea un test, utilizando las herramientas de tu lenguaje, que sea
#  * capaz de determinar si esa función se ejecuta correctamente.
#  *
import unittest

lista = [11,24]
lista2 = [33,12]

def sumar(numeros):
    return sum(numeros)

#Usando assert :sierve para hacer comprobaciones______________________
# print(sumar(lista))
# assert(sumar(lista)==35) # en caso sea incorrecto lanzara una excepcion

#Usando unittest______________________________________
'''
para usar correctamente el unittest , el archivo tiene que empezar con test_ y
ademas las funciones de prueba dentro de la clase que se crea para probar la funcion 
tambien ya que al momento de ejcutar python -m unittest discover -v para ver mas en 
detalle las pruebas no encontrara nada, por lo tanto es importante que se pueda hacer esas correcciones

tenemos diversos metodos para unittest como .assertTrue(x) , .assertFalse(x) , .assertIsNone(x) , .assertRaises(x)
''' 
class TestSuma(unittest.TestCase):
    def test_1(self):
        resultado = sumar(lista)
        self.assertEqual(resultado,35)

    def test_2(self):
        resultado = sumar(lista2)
        self.assertEqual(resultado,45)

    def test_3(self):
        
        self.assertIn(12,lista2)
    

#  * DIFICULTAD EXTRA (opcional):
#  * Crea un diccionario con las siguientes claves y valores:
#  * "name": "Tu nombre"
#  * "age": "Tu edad"
#  * "birth_date": "Tu fecha de nacimiento"
#  * "programming_languages": ["Listado de lenguajes de programación"]
#  * Crea dos test:
#  * - Un primero que determine que existen todos los campos.
#  * - Un segundo que determine que los datos introducidos son correctos.
#  */

diccionario = {
        "nombre" : "Martin",
        "edad" : 23,
        "fecha_nacimiento" : "12-01-2002",
        "lenguajes" : ["Python","Java","PHP", "Rust","Go","Perl","Ruby","C","C++","C#"]
        }

class Test_diccionario(unittest.TestCase):
    def test_campos_existentes(self):
        campos = {"nombre","edad","fecha_nacimiento","lenguajes"}

        self.assertEqual(set(diccionario.keys()),campos)

    def test_datos_correctos(self):
        self.assertIsInstance(diccionario["nombre"],str)
        self.assertIsInstance(diccionario["edad"],int)
        self.assertIsInstance(diccionario["fecha_nacimiento"],str)
        self.assertIsInstance(diccionario["lenguajes"],list)


if __name__ == '__main__':
    unittest.main()