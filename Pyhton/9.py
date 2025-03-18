# /*
#  * EJERCICIO:
#  * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
#  * implemente una superclase Animal y un par de subclases Perro y Gato,
#  * junto con una función que sirva para imprimir el sonido que emite cada Animal.
#  *



#HERENCIA
class Animal:
    def __init__(self,nombre,especie,edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    def sonido(self):
        pass
    #Heredados para todas las clases hijas   
    def descripcion(self):
        print(f"Soy un {type(self).__name__} me llamo : {self.nombre} y tengo: {self.edad} años")

class Perro(Animal):
    '''
    para inicializar una nueva variable en una subclase, se debe crear el inicializador en donde se coloca todos los parametros,
    agregando el nuevo parametro, y dentro de ella usar super() para llamar al __init__ del padre y asi solo asignar la nueva variable
    '''
    def __init__(self, nombre, especie, edad,dueño): # agregamos la variable dueño
        super().__init__(nombre, especie, edad) # __init__ del padre
        self.dueño = dueño # nueva variable

    #Heredados de la clase padre pero modificadas
    def sonido(self):
        print("Sonido que hace: Guaauu")
    
    def descripcion(self):
        print(f"Soy un {type(self).__name__} me llamo : {self.nombre}, tengo: {self.edad} años y mi dueño es {self.dueño}")

class Gato(Animal):
    #Heredados de la clase padre pero modificadas
    def sonido(self):
        print("Sonido que hace: Miaaau")


perro1 = Perro("Zeus","mamifero",9,"Carlos")
perro1.descripcion()
perro1.sonido()


gato1 = Gato("Pelusa","mamifero",3)
gato1.descripcion()
gato1.sonido()


#  * DIFICULTAD EXTRA (opcional):
#  * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
#  * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
#  * Cada empleado tiene un identificador y un nombre.
#  * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
#  * actividad, y almacenan los empleados a su cargo.
#  */


class Empleado:
    def __init__(self,id ,nombre):
        self.id = id
        self.nombre = nombre

    def mostrar_datos(self):
        return f"id : {self.id} Nombre: {self.nombre}"

    

class Gerente(Empleado):
    def __init__(self, id, nombre):
        super().__init__(id, nombre)
        self.empleado_acargo = []

    def agregar_empleado(self,empleado):
        self.empleado_acargo.append(empleado)

    def mostrar_equipo(self):
        print(f"El equipo del gerente {self.nombre} es: {", ".join(e.nombre for e in self.empleado_acargo)}")


class Gerente_Proyecto(Empleado):
    def __init__(self, id, nombre,proyectos=None):
        super().__init__(id, nombre)
        self.proyectos = proyectos if proyectos else []

    def agregar_proyectos(self,proyecto):
        self.proyectos.append(proyecto)

    def mostrar_proyectos(self):
        print(f"{self.nombre} , tiene proyectos a cargo: {", ".join(self.proyectos)}")


class Programador(Empleado):
    def __init__(self, id, nombre,lenguaje):
        super().__init__(id, nombre)
        self.lenguaje = lenguaje


    def desarrollar_funcionalidades(self):
        print(f"Desarrollando funcionalidades con: {self.lenguaje}")



gerente1 = Gerente(1,"Juan Masias")

gerente_pro1 = Gerente_Proyecto(2,"Paco Yunque")
gerente_pro1.agregar_proyectos("Sistema de hoteles")
gerente_pro1.agregar_proyectos("Chatbot de la UNPRG")


programador1= Programador(4,"Joaquin Riva","Python")
programador2= Programador(5,"Robertiño gaaa", "Python")
programador3 = Programador(6,"Luis Arevales" ,"Java")
programador4 = ProcessLookupError(7,"Elver Quiroz", "PHP")

#agregando emepleados a cargo del gerente1:
gerente1.agregar_empleado(gerente_pro1)
gerente1.agregar_empleado(programador1)
gerente1.agregar_empleado(programador2)



gerente1.mostrar_equipo()
gerente_pro1.mostrar_proyectos()

programador1.desarrollar_funcionalidades()
programador2.desarrollar_funcionalidades()
programador3.desarrollar_funcionalidades()

