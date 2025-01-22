"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """

import pandas as pd
import re

def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requerimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.

    """







    clusters = []
    cantidades = []
    porcentajes = []
    palabras_claves = []

    cluster = None
    keywords = []

    with open('files/input/clusters_report.txt', 'r') as f:
        lines = f.readlines()

    # Inicializar las listas para almacenar los datos
    clusters = []
    cantidades = []
    porcentajes = []
    palabras_claves = []

    # Variables temporales para almacenar datos entre líneas
    current_cluster = None
    current_keywords = []

    # Iterar sobre las líneas
    for line in lines:
        line = line.strip()
        
        # Si la línea está vacía, la ignoramos
        if not line:
            continue
        
        # Si la línea comienza con un número, es el inicio de un nuevo cluster
        if line[0].isdigit():
            # Si ya tenemos un cluster anterior, agregamos sus datos
            if current_cluster is not None:
                clusters.append(current_cluster)
                cantidades.append(current_cantidad)
                porcentajes.append(current_porcentaje)                
                palabras_claves.append(', '.join(current_keywords))
            
            # Extraer el número del cluster, la cantidad y el porcentaje
            parts = re.split(r'\s{2,}', line)
            cluster_number = int(parts[0].strip())
            cantidad = int(parts[1].strip())
            porcentaje = parts[2].strip()
            # Limpiar el porcentaje y extraer el número
            porcentaje_value = re.sub(r'[^\d.]', '', porcentaje)
            
            # Iniciar la acumulación de palabras clave
            current_cluster = cluster_number
            current_cantidad = cantidad
            current_porcentaje = porcentaje_value
            
            # Asegurarse de que las primeras palabras clave estén en el cluster
            current_keywords = parts[3].split(', ')  # Extraer las primeras palabras clave del mismo campo 
        else:
            # Si no empieza con número, es continuación de las palabras clave
            current_keywords.extend(line.strip().split(', '))

    # Agregar el último cluster
    if current_cluster is not None:
        clusters.append(current_cluster)
        cantidades.append(current_cantidad)
        porcentajes.append(current_porcentaje)
        palabras_claves.append(', '.join(current_keywords))

    

    # Crear el DataFrame
    df = pd.DataFrame({
        'cluster': clusters,
        'cantidad_de_palabras_clave': cantidades,
        'porcentaje_de_palabras_clave': porcentajes,
        'principales_palabras_clave': palabras_claves
    })

    # Devolver el DataFrame resultante
    return df

# Llamar a la función y mostrar el resultado


df = pregunta_01()
print(df.principales_palabras_clave.to_list()[0])