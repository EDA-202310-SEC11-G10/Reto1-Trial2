"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def new_data_structs():
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    data_structs = {"Anios": {}, "Subsector_economico": {}}
    data_structs["data"] = lt.newList(datastructure='ARRAY_LIST', cmpfunction=compare)
    
    return data_structs


# Funciones para agregar informacion al modelo

def add_data(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    d = new_data(data["Año"], data["Código actividad económica"], data["Nombre actividad económica"],
                 data["Código sector económico"], data["Nombre sector económico"], data["Código subsector económico"],
                 data["Nombre subsector económico"], data["Total ingresos netos"], data["Total costos y gastos"],
                 data["Total saldo a pagar"], data["Total saldo a favor"], data["Total retenciones"])
    
    if data["Año"] in data_structs["Anios"]:
        lt.addLast(data_structs["Anios"][data["Año"]], d)
          
    else:
        data_structs["Anios"][data["Año"]] = lt.newList(datastructure='ARRAY_LIST', cmpfunction=compare)
        lt.addLast(data_structs["Anios"][data["Año"]], d)

    lt.addLast(data_structs["data"], d)
    
    if data["Código subsector económico"] in data_structs["Subsector_economico"]:
        lt.addLast(data_structs["Subsector_economico"][data["Código subsector económico"]], d)
          
    else:
        data_structs["Subsector_economico"][data["Código subsector económico"]] = lt.newList(datastructure='ARRAY_LIST', cmpfunction=compare)
        lt.addLast(data_structs["Subsector_economico"][data["Código subsector económico"]], d)

    return data_structs

# Funciones para creacion de datos

def new_data(año, codigo, nom_act_ec, codigo_sec_ec,nombre_sec_ec, codigo_subsector,nombre_sebsector,
             total_ingr_netos, total_costos_gastos,saldo_a_pagar, saldo_favor,total_retenciones):
    """
    Crea una nueva estructura para modelar los datos
    """
    data = {}
    data["Año"] = año
    data["Código actividad económica"] = codigo
    data["Nombre actividad económica"] = nom_act_ec
    data["Código sector económico"] = codigo_sec_ec
    data["Nombre sector económico"] = nombre_sec_ec
    data["Código subsector económico"]= codigo_subsector
    data["Nombre subsector económico"] = nombre_sebsector
    data["Total ingresos netos"] = total_ingr_netos
    data["Total costos y gastos"] = total_costos_gastos
    data["Total saldo a pagar"] = saldo_a_pagar
    data["Total saldo a favor"] = saldo_favor
    data["Total retenciones"] = total_retenciones

    return data


# Funciones de consulta

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    #TODO: Crear la función para obtener un dato de una lista
    pass


def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    filas = 0
    for impuesto in data_structs["data"]["elements"]:
        filas += 1
        
    return filas

def req_1(data_structs):
    """
    Función que soluciona el requerimiento 1
    """
    respuestas = {}
    respuestas["data"] = lt.newList(datastructure='ARRAY_LIST')
    
    for llave_año in data_structs["Anios"]:
        mayor = 0
        listas_actvidades_por_año = data_structs["Anios"][llave_año]["elements"]
        for actividad in listas_actvidades_por_año:
            total_saldo_pagar = actividad["Total saldo a pagar"]
            total_saldo_a_pagar = int(total_saldo_pagar)
            if  total_saldo_a_pagar > mayor:
                mayor = total_saldo_a_pagar
                resp = actividad
            
        lt.addLast(respuestas["data"],resp)
        
    merg.sort(respuestas["data"], sort_criteria)
    
    return respuestas


def req_2(data_structs):
    """
    Función que soluciona el requerimiento 2
    """
    return data_structs


def req_3(data_structs):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    pass


def req_4(data_structs):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    pass


def req_5(data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    pass


def req_6(data_structs):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    pass


def req_7(data_structs):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    pass


def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass


# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2, id):
    """
    Función encargada de comparar dos datos
    """
    if data_1[id] < data_2[id]:
        return True
    elif data_1[id] > data_2[id]:
        return False
    else:
        return "equal"


# Funciones de ordenamiento


def sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    return cmp_impuestos_by_anio_CAE(data_1, data_2)


def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    return merg.sort(data_structs["data"], sort_criteria)

def cmp_impuestos_by_anio_CAE(data_1, data_2):
    year = compare(data_1, data_2, "Año")
    if year == "equal":
        return compare(data_1, data_2, "Código actividad económica")
    else:
        return year
    