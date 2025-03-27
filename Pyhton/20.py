# /*
#  * EJERCICIO:
#  * Utilizando un mecanismo de peticiones HTTP de tu lenguaje, realiza
#  * una petición a la web que tú quieras, verifica que dicha petición
#  * fue exitosa y muestra por consola el contenido de la web.
#  *

# direccion = "https://jsonplaceholder.typicode.com/posts/1"
# direccion2 = "https://www.google"        

#obtner_respuesta(direccion3)


#  * DIFICULTAD EXTRA (opcional):
#  * Utilizando la PokéAPI (https://pokeapi.co), crea un programa por
#  * terminal al que le puedas solicitar información de un Pokémon concreto
#  * utilizando su nombre o número.
#  * - Muestra el nombre, id, peso, altura y tipo(s) del Pokémon
#  * - Muestra el nombre de su cadena de evoluciones
#  * - Muestra los juegos en los que aparece
#  * - Controla posibles errores
#  */
import requests

direccion3 = "https://pokeapi.co/api/v2/"

def obtener_respuesta(url):
    try:
        respuesta = requests.get(url)
        if respuesta.status_code != 200:
            print(f"NO SE PUEDE CONECTAR A LA PAGINA, Error: {respuesta.status_code}")
            return None
        try:
            return respuesta.json()
        except requests.exceptions.JSONDecodeError:
            return respuesta.text
    except requests.exceptions.RequestException as e:
        print(f"Error en la conexion: {e}")
        return None


def mostrar_evoluciones(inicio):
    
    print(f" - {inicio['species']['name']}")
    if inicio.get("evolves_to"):
        for evolucion in inicio["evolves_to"]:
            mostrar_evoluciones(evolucion)

def buscar_pokemon_datos():
    pokemon = input("Ingresa el nombre o número de Pokémon a buscar: ").strip().lower()

    # Obtener datos básicos del Pokémon
    url_pokemon = f"{direccion3}pokemon/{pokemon}"
    respuesta = obtener_respuesta(url_pokemon)
    if not respuesta:
        print("Pokémon no encontrado")
        return

    print(f"Nombre: {respuesta['name']}")
    print(f"ID: {respuesta['id']}")
    print(f"Peso: {respuesta['weight']}")
    print(f"Altura: {respuesta['height']}")
    print("Tipos:")
    for i, tipo in enumerate(respuesta.get("types", []), 1):
        print(f"  {i}. {tipo['type']['name']}")

    url_especie = f"{direccion3}pokemon-species/{pokemon}"
    datos_especie = obtener_respuesta(url_especie)
    if datos_especie and "evolution_chain" in datos_especie:

        url_evolucion = datos_especie["evolution_chain"]["url"]
        respuesta_evol = obtener_respuesta(url_evolucion)

        if respuesta_evol and "chain" in respuesta_evol:
            print(f"Cadena de evolución de {respuesta['name']}:")
            mostrar_evoluciones(respuesta_evol["chain"])
        else:
            print("No se encontró información de la cadena de evolución")
    else:
        print("No se encontró información de la cadena de evolución")

 
    print("Juegos en los que aparece:")
    for i, juego in enumerate(respuesta.get("game_indices", []), 1):
        print(f"  {i}. {juego['version']['name']}")

buscar_pokemon_datos()
