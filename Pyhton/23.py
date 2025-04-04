# /*
#  * EJERCICIO:
#  * Explora el patrón de diseño "singleton" y muestra cómo crearlo
#  * con un ejemplo genérico.
#  *


#USANDO CLASES

class Singleton1:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance


class Singleton1:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton1,cls).__new__(cls)

        return cls._instance

objeto1 = Singleton1()
objeto2 = Singleton1()

print(objeto1 is objeto2)


#USANDO DECORADOR
def singleton2(cls):
    instances = {}

    def get_instance(*args , **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        
        return instances[cls]
    return get_instance

@singleton2
class Singleton2:
    pass

objeto3 = Singleton2()
objeto4 = Singleton2()
print(objeto3 is objeto4)



#USANDO METACLASES
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Singleton3(metaclass=SingletonMeta):
    pass

# Prueba
objeto5 = Singleton3()
objeto6 = Singleton3()
print(objeto5 is objeto6)


#  * DIFICULTAD EXTRA (opcional):
#  * Utiliza el patrón de diseño "singleton" para representar una clase que
#  * haga referencia a la sesión de usuario de una aplicación ficticia.
#  * La sesión debe permitir asignar un usuario (id, username, nombre y email),
#  * recuperar los datos del usuario y borrar los datos de la sesión.
#  */


class UsuarioSesion(metaclass=SingletonMeta):
    def __init__(self):
        self.datos_usuario = None
    
    def login(self, id, username, nombre, email):
        if self.datos_usuario:
            print("Ya existe un usuaio en la sesion")
            return
        self.datos_usuario = {
            "id" : id,
            "username" : username,
            "nombre" : nombre,
            "email" : email
        }

    def obtener_usuario(self):
        if not self.datos_usuario:
            print("No existe usuario para obtener datos :c")
            return None
        
        return self.datos_usuario
    
    def salir_sesion(self):
        if not self.datos_usuario:
            print("No existe usuario para cerrar sesion uwu")
            return
        print(f"{self.datos_usuario["username"]} ha cerrado sesion aña")
        self.datos_usuario = None


sesion = UsuarioSesion()
sesion.login(1,"mdsus","martin lozano","marts@gamil.com")

print(sesion.obtener_usuario())

sesion2 = UsuarioSesion()

sesion.salir_sesion()
print(sesion2.obtener_usuario())


