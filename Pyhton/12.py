# /*
#  * IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
#  * 
#  * EJERCICIO:
#  * Desarrolla un programa capaz de crear un archivo XML y JSON que guarde los
#  * siguientes datos (haciendo uso de la sintaxis correcta en cada caso):
#  * - Nombre
#  * - Edad
#  * - Fecha de nacimiento
#  * - Listado de lenguajes de programación
#  * Muestra el contenido de los archivos.
#  * Borra los archivos.
#  *

import xml.etree.ElementTree as ET
import xml.dom.minidom
import os
import json

ARCHIVO_XML="datos.xml"
ARCHIVO_JSON="datos2.json"

datos = {
        "nombre" : "Martin",
        "edad" : 23,
        "fecha_nacimiento" : "12-01-2002",
        "lenguajes" : ["Python","Java","PHP", "Rust","Go","Perl","Ruby","C","C++","C#"]
        }

# PARA XML ________________________________________________________
def crear_xml():
    if  os.path.exists(ARCHIVO_XML):
        print("XML ya existe")
        return
    #definimos una raiz para el archivo xml:
    raiz = ET.Element("datos")

    #definimos los elementos principales:
    ET.SubElement(raiz,"nombre").text = datos['nombre']
    ET.SubElement(raiz,"edad").text = str(datos['edad'])
    ET.SubElement(raiz,"fecha_nacimiento").text = datos['fecha_nacimiento']

    #creamos una sub raiz lenguajes para listar todos los lenguajes
    leguajes_elemento = ET.SubElement(raiz,"lenguajes")
    for lenguaje in datos['lenguajes']:
        ET.SubElement(leguajes_elemento,"lenguaje").text = lenguaje

    #remplazamos la parte del arbol para dar formato a lo que se va a guardar en el xml
    xml_str = ET.tostring(raiz, encoding="utf-8")
    xml_pretty = xml.dom.minidom.parseString(xml_str).toprettyxml(indent="  ")

    #arbol = ET.ElementTree(raiz)
    #arbol.write(ARCHIVO_XML,encoding="UTF-8",xml_declaration=True)
    with open(ARCHIVO_XML,"w",encoding="UTF-8") as archivo_xml:
        archivo_xml.write(xml_pretty)
    print("XML creado")

def mostar():
    if  not os.path.exists(ARCHIVO_XML):
        print("XML no existe para eliminar")
        return
    with open(ARCHIVO_XML,"r",encoding="UTF-8") as xml:
        print(xml.read())

def eliminar():
    if  not os.path.exists(ARCHIVO_XML):
        print("XML no existe para eliminar")
        return
    os.remove("datos.xml")
    print("XML eliminado")


crear_xml()
# mostar()
# eliminar()



# PARA JSON ________________________________________________________

def crear_json():
    if os.path.exists(ARCHIVO_JSON):
        print("JSON ya existe")
        return
    with open(ARCHIVO_JSON,"w",encoding="UTF-8") as archivo_json:
        #dum permite que le pasemos un objeto y que lo pueda escribir en formato json
        json.dump(datos,archivo_json,indent=2,ensure_ascii=False)
    print("JSON CREADO")

def mostrar_json():
    if not os.path.exists(ARCHIVO_JSON):
        print("JSON no existe para mostrar")
        return
    
    with open(ARCHIVO_JSON,"r",encoding="UTF-8") as archivo_json:
        print(archivo_json.read())

def eliminar_json():
    if not os.path.exists(ARCHIVO_JSON):
        print("JSON no existe para eliminar")
        return
    os.remove(ARCHIVO_JSON)
    print("Archivo JSON eliminado")

crear_json()
# mostrar_json()
# eliminar_json()

#  * DIFICULTAD EXTRA (opcional):
#  * Utilizando la lógica de creación de los archivos anteriores, crea un
#  * programa capaz de leer y transformar en una misma clase custom de tu 
#  * lenguaje los datos almacenados en el XML y el JSON.
#  * Borra los archivos.
#  */

class Persona:
    def __init__(self,nombre,edad,fecha_nacimiento,lenguajes):
        self.nombre = nombre
        self.edad = edad
        self.fecha_nacimiento = fecha_nacimiento
        self.lenguajes = lenguajes
    
    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Fecha nacimiento: {self.fecha_nacimiento}")
        print("Lenguajes de programacion")
        for i,lenguaje in enumerate(self.lenguajes,1):
            print(f"{i}. {lenguaje}")

def obtener_datos_json():
    if not os.path.exists(ARCHIVO_JSON):
        print("NO EXISTE JSON PARA EXTRAER")
        return
    
    with open(ARCHIVO_JSON,"r") as archivo:
        datos_json = json.load(archivo)
    
    persona_json = Persona(datos_json["nombre"],datos_json["edad"],datos_json["fecha_nacimiento"],datos_json["lenguajes"])

    print(f"De JSON a una clase: {persona_json}")
    persona_json.mostrar_datos()

def obtener_datos_xml():
    if not os.path.exists(ARCHIVO_XML):
        print("NO EXISTE XML PARA EXTRAER")
        return

    archivo = ET.parse(ARCHIVO_XML)
    raiz = archivo.getroot()
    lenguajes = [l.text for l in raiz.find("lenguajes").findall("lenguaje")]
    persona_xml = Persona(raiz.find("nombre").text,int(raiz.find("edad").text),raiz.find("fecha_nacimiento").text,lenguajes)

    print(f"De XML a una clase: {persona_xml}")
    persona_xml.mostrar_datos()

def eliminar_archivos():

    for archivo in [ARCHIVO_XML,ARCHIVO_JSON]:
        if os.path.exists(archivo):
            os.remove(archivo)
            
        print("ARCHIVOS ELIMINADOS")
    else:
        print("no se encontro aña")


obtener_datos_json()
obtener_datos_xml()
eliminar_archivos()