# /*
#  * EJERCICIO:
#  * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
#  * - Utiliza operaciones de inserción, borrado, actualización y ordenación.

# LISTA__________________________________________
lista = [0,2,90,11,19.3,900,13,124312, 190.23]

#insercion
lista.append(12)
lista.insert(3,17) #insertar por indice
print(lista)

#borrado
lista.remove(0) #borrar por valor
del lista[4] 
print(lista)

#actualizacion
lista[5] = 128
print(lista)

#ordenacion
lista.sort() #orden ascendente
print(lista)

#TUPLA__________________________________________
tupla = (0,2,90,11,19.3,900,13,124312, 190.23)

#insercion
#una tupla es inmutable, osea no se puede agregar mas elementos

#CONJUNTO__________________________________________
conjunto = {0,2,90,11,19.3,900,13,124312, 190.23}

conjunto.add(79)
print(conjunto)

#borrado
conjunto.remove(11) #lanza error si esque no existe el 11
conjunto.discard(900) #no lanza error en caso no exista el elemento
print(conjunto)

#actualizacion
conjunto.update([69,6])
print(conjunto)

#ordenacion
conjunto_ordenado = sorted(conjunto)
print(conjunto_ordenado)



#DICCIONARIO__________________________________________
diccionario = {'Nombre':'Martín de Jesús',
               'Apellidos':'Lozano Silvestre',
               'Edad':23}

#insercion
diccionario['Direccion'] = "Junin 569"
print(diccionario)

#borrado
del diccionario['Edad']
print(diccionario)

#actualizacion
diccionario['Direccion'] = "Angamos 345"
print(diccionario)

#ordenacion
diccionario_ordenado = dict(sorted(diccionario.items()))
print(diccionario_ordenado)


# * DIFICULTAD EXTRA (opcional):
#  * Crea una agenda de contactos por terminal.
#  * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
#  * - Cada contacto debe tener un nombre y un número de teléfono.
#  * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
#  *   los datos necesarios para llevarla a cabo.
#  * - El programa no puede dejar introducir números de teléfono no numéricos y con más de 11 dígitos.
#  *   (o el número de dígitos que quieras)
#  * - También se debe proponer una operación de finalización del programa.
#  */

Agenda = []

def menu():
    print("AGENDA DE CONTACTOS")
    print("1.Agregar contacto")
    print("2.Buscar contacto")
    print("3.Modificar contacto")
    print("4.Eliminar contacto")
    print("5.Salir")

def agregar_contacto():

    while True:
        listar_contato() if Agenda else print("No existe contactos en la agenda, Registra uno")
        
        nombre = input("Ingrese nombre: ").strip().lower()
        if not nombre :
            print("No puede estar vacío el campo o campos.")
            continue

        while True:
            try:
                numero = input("Ingrese numero: ").strip()
                if not numero.isdigit():
                    print("Solo se permiten numeros")
                    continue
                if len(numero) < 11 :
                    print("El numero debe ser mayor a 11")
                    continue
                break
            except ValueError:
                print("Ingresa un numero valido")

        contacto = {"nombre": nombre, "numero": numero}

        if contacto in Agenda :
            print(f"Contacto ya existe")
        else:
            Agenda.append(contacto)
            print(f"Contacto registrado\n")
        if input("¿Quieres registrar otro contacto? (S/N):").strip().lower() != "s":
            break  

def buscar_contacto():
    while True:
        busqueda = input("Ingrese nombre o numero a buscar: ").strip().lower()

        contacto = retornar_contacto(busqueda)

        if contacto != -1:
            print(f"Nombre : {contacto['nombre']}\nNumero : {contacto['numero']}")
        else:
            print("No se encontro al contacto")

        if input("¿Quieres buscar otro contacto? (S/N):").strip().lower() != "s":
            break

def  modificar_contacto():
    while True:
        listar_contato() if Agenda else print("No existe contactos en la agenda, Registra uno")

        numero = int(input("Contacto que quiere modificar: "))

        contacto = retornar_contacto(numero)

        if contacto!=-1:
            print(f"Nombre actual: {contacto['nombre']}")
            nuevo_nombre = input("Escribe nuevo nombre (o preciona Enter para mantenerlo) : ").strip().lower()
            
            print(f"Numero actual: {contacto['numero']}")
            nuevo_numero = input("Escribe nuevo numero (o preciona Enter para mantenerlo) : ").strip().lower()

            contacto['nombre'] = nuevo_nombre if nuevo_nombre else contacto['nombre']
            contacto['numero'] = nuevo_numero if nuevo_numero else contacto['numero']

            print("DATOS ACTUALIZADOS")

            print(f"Nombre : {contacto['nombre']}\nNumero : {contacto['numero']}")

        else:
            print("No se encontro al contacto")

        if input("¿Quieres modificar otro contacto? (S/N):").strip().lower() != "s":
            break

def eliminar_contacto():
    while True:
        listar_contato() if Agenda else print("No existe contactos en la agenda, Registra uno")

        numero = int(input("Contacto que quiere eliminar: "))

        contacto = retornar_contacto(numero)
        print(f"Nombre : {contacto['nombre']}\nNumero : {contacto['numero']}")

        if contacto != -1:
            if input("¿Estas seguro de eliminar este contacto? (S/N):").strip().lower() != "s":
                continue

            Agenda.remove(contacto)
            print("CONTACTO ELIMINADO")
        else:
            print("contacto no encontrado")

        if input("¿Quieres eliminar otro contacto? (S/N):").strip().lower() != "s":
            break


def listar_contato():
    print("CONTACTOS REGISTRADOS")
    for i,contacto in enumerate(Agenda,1):
        print(f"{i} - {contacto['nombre'].capitalize()} {contacto['numero']}")

def retornar_contacto(dato):
    if isinstance(dato,str):
        for contacto in Agenda:
            if contacto['nombre'] == dato or contacto['numero'] == dato :
                return contacto
        return -1
    else:
        return Agenda[dato-1] if 1<= dato <= len(Agenda) else -1 


#def retornar_contacto_id(numero):


def main():
    while True:
        menu()

        try:
            opcion = int(input("Seleccione: "))
        except ValueError:
            print("Error, ingrese un número válido")
            continue

        if opcion == 1:
            agregar_contacto()
        elif opcion == 2:
            buscar_contacto()
        elif opcion == 3:
            modificar_contacto()
        elif opcion == 4:
            eliminar_contacto()
        elif opcion == 5:
            print("Saliendo")
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    main()