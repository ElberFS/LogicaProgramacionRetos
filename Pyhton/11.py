# /*
#  * IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
#  * 
#  * EJERCICIO:
#  * Desarrolla un programa capaz de crear un archivo que se llame como
#  * tu usuario de GitHub y tenga la extensión .txt.
#  * Añade varias líneas en ese fichero:
#  * - Tu nombre.
#  * - Edad.
#  * - Lenguaje de programación favorito.
#  * Imprime el contenido.
#  * Borra el fichero.

import os
# archivo = "archivos\\texto.txt"
# #con "w" se sobre escribe en el archivo inicial, con "a" se agrega en el archivo, y con "x" se crea el archivo solo si no existe
# diccionario1 = {"Nombre" : "Martín de Jesús Lozano Silvestre",
#                 "Edad":23,
#                 "Lenguaje favorito":"Python"}


# def creando_archivo():
#     try:
#         with open(archivo,"x",encoding="UTF-8") as texto:
#             for key,value in diccionario1.items():
#                 texto.write(f"{key} : {value}\n")
#         print("Archivo creado correctamente")
#     except FileExistsError:
#         print("El archivo ya existe")

# def leer_archivo():
#     try:
#         with open(archivo,encoding="UTF-8") as texto:
#             print(texto.read())
#     except FileNotFoundError:
#         print("Archivo no existe")


# def eliminar_archivo():
#     try:
#         os.remove(archivo)
#         print("Archivo eliminado correctamente")
#     except FileNotFoundError:
#         print("Archivo no existe")

# creando_archivo()
#leer_archivo()
#eliminar_archivo()



#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Desarrolla un programa de gestión de ventas que almacena sus datos en un 
#  * archivo .txt.
#  * - Cada producto se guarda en una línea del archivo de la siguiente manera:
#  *   [nombre_producto], [cantidad_vendida], [precio].
#  * - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
#  *   actualizar, eliminar productos y salir.
#  * - También debe poseer opciones para calcular la venta total y por producto.
#  * - La opción salir borra el .txt.
#  */

import os
ARCHIVO2 = "archivos\\ventas.txt"


def menu():
    print("GESTION DE VENTAS")
    print("1.Agregar producto")
    print("2.Buscar producto")
    print("3.Actualizar producto")
    print("4.Eliminar producto")
    print("5.Mostrar informes")
    print("6.Salir")


def buscar_similitudes(nombre):
    with open(ARCHIVO2,"r",encoding="UTF-8") as texto:
        for linea in texto:
            datos = linea.strip().split(", ")
            if datos[0].lower() == nombre.lower():
                return True
            
    return False

def buscar_producto(nombre):
    with open(ARCHIVO2,"r",encoding="UTF-8") as texto:
        for linea in texto:
            datos = linea.strip().split(", ")
            if datos[0].lower() == nombre.lower():
                return {"nombre": datos[0], "cantidad_vendida":datos[1], "precio_unitario":datos[2]}
    return None


def listar_en_archivo():
    try:
        with open(ARCHIVO2,encoding="UTF-8") as texto:
            print(texto.read())
    except FileNotFoundError:
        print("Archivo no existe")

def agregar():
    while True:
        nombre = input("Nombre de producto: ").strip().lower()

        if os.path.exists(ARCHIVO2):
            contenido = buscar_similitudes(nombre)
            if contenido == True:
                print("Nombre ya existe")
                continue
        

        while True:
            try:
                cant_vendida = int(input("Cantidad vendida: "))
                precio = float(input("Precio unitario: "))
                if cant_vendida <= 0 or precio<=0:
                    print("El valor debe ser positivo")
                    continue
                break
            except ValueError:
                print("Ingrese un numero valido")
                continue


        if not os.path.exists(ARCHIVO2):
            with open(ARCHIVO2,"x",encoding="UTF-8") as texto:
                texto.write(f"{nombre}, {cant_vendida}, {precio}\n")
            print("Archivo creado exitosamente")
            print("Producto agregado")

        else:
            with open(ARCHIVO2,"a",encoding="UTF-8") as texto:
                texto.write(f"{nombre}, {cant_vendida}, {precio}\n")
            print("Producto Agregado")
        
        if input("¿Quieres agregar otro producto? (S/N):").strip().lower() != "s":
            break


def consultar():
    listar_en_archivo() if os.path.exists(ARCHIVO2) else print("No existe archivo para leer")

    while True:
        producto = input("Ingrese el nombre de producto a consultar: ")

        resultado = buscar_producto(producto)

        if resultado:
            print(f"Nombre: {resultado['nombre']}")
            print(f"Cantidad Vendida: {resultado['cantidad_vendida']}")
            print(f"Precio unitario: {resultado['precio_unitario']}")
        else:
            print("Producto no encontrado")
        
        if input("¿Quieres buscar otro producto? (S/N):").strip().lower() != "s":
            break

def actualizar():
    print("Productos a actualizar")
    listar_en_archivo() if os.path.exists(ARCHIVO2) else print("No existe archivo para leer")
    
    while True:

        productos = []
        with open(ARCHIVO2,"r",encoding="UTF-8") as texto:
            productos = texto.readlines()
        
        nombre = input("Nombre de producto a actualizar: ").strip().lower()
        actualizado = False

        with open(ARCHIVO2,"w",encoding="UTF-8") as texto:
            for linea in productos:
                datos = linea.strip().split(", ")

                if datos[0].lower() == nombre:
                    print(f"Nombre actual: {datos[0]}")
                    nuevo_nombre = input("Nuevo nombre o presiona espacio para mantenerlo: ")
                    print(f"Cantidad actual: {datos[1]}")
                    nueva_cantidad = input("Nueva cantidad o presiona espacio para mantenerlo: ")
                    print(f"Precio actual: {datos[2]}")
                    nuevo_precio = input("Nuevo precio o presiona espacio para mantenerlo: ")

                    datos[0] = nuevo_nombre if nuevo_nombre else datos[0]
                    datos[1] = nueva_cantidad if nueva_cantidad else datos[1]
                    datos[2] = nuevo_precio if nuevo_precio else datos[2]

                    texto.write(f"{", ".join(datos)}\n")
                    print("Producto actualizado")
                    actualizado = True
                else:
                    texto.write(linea)
        
        if not actualizado:
            print("Producto no encontrado")

        if input("¿Quieres buscar otro producto? (S/N):").strip().lower() != "s":
            break

def eliminar():
    print("Eliminar Productos")
    listar_en_archivo() if os.path.exists(ARCHIVO2) else print("No existe archivo para leer")

    productos = []
    with open(ARCHIVO2,"r",encoding="UTF-8") as texto:
        productos = texto.readlines()
    nombre = input("Nombre de producto a eliminar: ").strip().lower()
    eliminado = False

    with open(ARCHIVO2,"w",encoding="UTF-8") as texto:
        for linea in productos:
            datos = linea.strip().split(", ")
            if datos[0].lower() != nombre:
                texto.write(linea)
            else:
                eliminado = True
                print("Producto eliminado")

    if not eliminado:
        print("Producto no encontrado")

def calcular_ventas():
    total_venta = 0
    productos = {}

    with open(ARCHIVO2,"r",encoding="UTF-8") as texto:
        for linea in texto:
            datos = linea.strip().split(", ")
            nombre, cantidad, precio = datos[0], int(datos[1]), float(datos[2])

            venta_total_producto = cantidad*precio
            productos[nombre] = venta_total_producto
            total_venta += venta_total_producto
    print("Venta por producto :")
    for nombre,total in productos.items():
        print(f"{nombre}: S/.{total:.2f}")

    print(f"Venta total :S/.{total_venta:.2f}")

def main():
    while True:
        menu()
        try:
            opcion = int(input("Seleccione : "))
        except ValueError:
            print("Numero invalido")
            continue

        if opcion == 1:
            agregar()
        elif opcion == 2:
            consultar()
        elif opcion == 3:
            pass
            actualizar()
        elif opcion == 4:
            
            eliminar()
        elif opcion == 5:
            calcular_ventas()
            pass
        elif opcion == 6:
            print("Saliendo")

            if os.path.exists(ARCHIVO2):
                os.remove(ARCHIVO2)
            break
        else:
            print("Opción inválida")


if __name__ == "__main__":
    main()

        