import time
from functools import wraps

# Decorador para medir el tiempo de ejecución de una función
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Tiempo de ejecución de {func.__name__}: {end_time - start_time:.6f} segundos")
        return result
    return wrapper

# Función para imprimir un mensaje de bienvenida
def bienvenida():
    """
    Imprime un mensaje de bienvenida al curso de Python.
    """
    print("¡Bienvenido al curso de Python!")

# Función para imprimir argumentos posicionales y nombrados
def informacion_completa(*args, **kwargs):
    """
    Imprime los argumentos posicionales y nombrados recibidos.
    
    Args:
    *args: Argumentos posicionales.
    **kwargs: Argumentos nombrados.
    """
    print("Argumentos posicionales:", args)
    print("Argumentos nombrados:", kwargs)

# Función para presentar información de una persona
def presentar_persona(nombre, edad=30, ciudad="Ámsterdam"):
    """
    Presenta la información de una persona con nombre, edad y ciudad.
    
    Args:
    nombre (str): Nombre de la persona.
    edad (int, opcional): Edad de la persona (por defecto 30).
    ciudad (str, opcional): Ciudad de residencia (por defecto "Ámsterdam").
    """
    print(f"Hola, mi nombre es {nombre}, tengo {edad} años y vivo en {ciudad}.")

# Generador de cuadrados de números hasta n
def generar_cuadrados(n):
    """
    Genera los cuadrados de los números del 1 a n.
    
    Args:
    n (int): Número entero hasta el cual se generan los cuadrados.
    
    Yields:
    int: Cuadrado de cada número desde 1 hasta n.
    """
    for i in range(1, n+1):
        yield i * i

# Generador de diccionario con cuadrados de números pares hasta n
def generar_pares_dict(n):
    """
    Genera un diccionario con los cuadrados de los números pares desde 1 hasta n.
    
    Args:
    n (int): Número entero hasta el cual se generan los cuadrados de los pares.
    
    Returns:
    dict: Diccionario donde las claves son números pares y los valores sus cuadrados.
    """
    pares_dict = {}
    for i in range(1, n+1):
        if i % 2 == 0:
            pares_dict[i] = i * i
    return pares_dict

#?
def diccionario_longitudes(lista_nombres):
    """
    Genera un diccionario donde las claves son los nombres y los valores son las longitudes de esos nombres.
    
    Args:
    lista_nombres (list): Lista de nombres (cadenas de texto).
    
    Returns:
    dict: Diccionario donde las claves son nombres y los valores sus longitudes.
    """
    longitudes_dict = {}
    for nombre in lista_nombres:
        longitudes_dict[nombre] = len(nombre)
    return longitudes_dict

#?
if __name__ == "__main__":
    bienvenida()
    
    try:
        informacion_completa(1, 2, 3, nombre="Ali", edad=25)
    except TypeError as e:
        print(f"Error al imprimir información completa: {e}")
    
    presentar_persona("Abel")
    presentar_persona("Eduardo", 25, "Róterdam")
    presentar_persona("Ali", ciudad="Utrecht")
    
    cuadrados = generar_cuadrados(5)
    print("Cuadrados:", list(cuadrados))
    
    try:
        print("Diccionario de pares de cuadrados:", generar_pares_dict(10))
    except ValueError as e:
        print(f"Error al generar diccionario de pares: {e}")
    
    nombres = ["Ali", "Abel", "Eduardo", "Ana"]
    try:
        print("Diccionario de longitudes de nombres:", diccionario_longitudes(nombres))
    except Exception as e:
        print(f"Error al generar diccionario de longitudes: {e}")
