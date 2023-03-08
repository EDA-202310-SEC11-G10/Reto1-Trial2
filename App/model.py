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
                 data["Total saldo a pagar"], data["Total saldo a favor"], data["Total retenciones"],data["Costos y gastos nómina"])
    
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
             total_ingr_netos, total_costos_gastos,saldo_a_pagar, saldo_favor,total_retenciones,costos_gastos_nomina):
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
    data["Costos y gastos nómina"] = costos_gastos_nomina

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
    menores_año = {"data": lt.newList(datastructure='ARRAY_LIST')}
    
    for llave_año in data_structs["Anios"]:
        lista_subsectores = {"codigos": {}}
        
        listas_actvidades_por_año = data_structs["Anios"][llave_año]["elements"]
        for actividad in listas_actvidades_por_año:
            cod_sub_sector_ec = actividad["Código subsector económico"]
            
            if  cod_sub_sector_ec in lista_subsectores["codigos"]:
                lt.addLast(lista_subsectores["codigos"][cod_sub_sector_ec], actividad)
          
            else:
                lista_subsectores["codigos"][cod_sub_sector_ec] = lt.newList(datastructure='ARRAY_LIST', cmpfunction=compare)
                lt.addLast(lista_subsectores["codigos"][cod_sub_sector_ec], actividad)
          
        codigos = lista_subsectores["codigos"]
        retenciones_totales = 0
        dicc_año_retenciones_totales = {"data": lt.newList(datastructure='ARRAY_LIST')}
        
        for llaves in codigos:
            impuesto = codigos[llaves]["elements"]
            retenciones_totales = 0
            ingr_netos_totales = 0
            total_costos_gastos = 0
            total_saldo_por_pagar = 0
            total_saldo_favor = 0
            
            for elem in impuesto:
                año = elem["Año"]
                codigo_sec_econ = elem["Código sector económico"]
                nombre_sec_econ = elem["Nombre sector económico"]
                #codigo_subsector = elem["Código subsector económico"]
                nombre_subsector = elem["Nombre subsector económico"]
                
                ingr_netos = elem["Total ingresos netos"]
                costos_y_gastos = elem["Total costos y gastos"]
                saldo_por_pagar = elem["Total saldo a pagar"]
                saldo_favor = elem["Total saldo a favor"]
                
                retenciones_impuesto = elem["Total retenciones"]
                
                retenciones_impuesto = int(retenciones_impuesto)
                ingr_netos_impuesto = int(ingr_netos)
                costos_y_gastos = int(costos_y_gastos)
                saldo_por_pagar = int(saldo_por_pagar)
                saldo_favor = int(saldo_favor)
                
                
                retenciones_totales += retenciones_impuesto
                ingr_netos_totales += ingr_netos_impuesto
                total_costos_gastos += costos_y_gastos
                total_saldo_por_pagar +=  saldo_por_pagar
                total_saldo_favor += saldo_favor
                
            info = {}
            info["Año"] = año
            info["Código sector económico"] = codigo_sec_econ
            info["Nombre sector económico"] = nombre_sec_econ
            info["Código subsector económico"] = llaves
            info["Nombre subsector económico"] = nombre_subsector
            
            info["Total de retenciones del subsector económico"] = retenciones_totales
            info["Total ingresos netos del subsector económico"] = ingr_netos_totales
            info["Total costos y gastos del subsector económico"] =  total_costos_gastos
            info["Total saldo por pagar del subsector económico"] = total_saldo_por_pagar
            info["Total saldo a favor del subsector económico"] = total_saldo_favor
            
            lt.addLast(dicc_año_retenciones_totales["data"],info)
            
        merg.sort(dicc_año_retenciones_totales["data"],sort_criteria_retencion)
        menor_por_año = lt.firstElement(dicc_año_retenciones_totales["data"])
        lt.addLast(menores_año["data"], menor_por_año)
        
    merg.sort(menores_año["data"],sort_criteria)
    
    return menores_año

def req_2b(data_structs):
    
    lista_global  =lt.newList(datastructure='ARRAY_LIST')

    for llave_años in data_structs["Anios"]:
        lista_primeros_y_ultimos = lt.newList(datastructure='ARRAY_LIST')
        lista_años = lt.newList(datastructure='ARRAY_LIST')
        lista_por_años = data_structs["Anios"][llave_años]["elements"]
        
        for actividad in lista_por_años:
            lt.addLast(lista_años, actividad)
            
            merg.sort(lista_años, sort_criteria_retencion_AÑO)
        
        for i in range(0,3):
            actividad = lt.getElement(lista_años,1)
            lt.addLast(lista_primeros_y_ultimos, actividad)
            lt.removeFirst(lista_años)
        
        lt.addLast(lista_global, lista_primeros_y_ultimos)
        
    return lista_global


def req_3(data_structs):
    """
    Función que soluciona el requerimiento 3
    """
    mayores_nomina= {"data": lt.newList(datastructure='ARRAY_LIST')}
    
    for llave_año in data_structs["Anios"]:
        lista_subsectores = {"codigos": {}}
        
        listas_actvidades_por_año = data_structs["Anios"][llave_año]["elements"]
        for actividad in listas_actvidades_por_año:
            cod_sub_sector_ec = actividad["Código subsector económico"]
            
            if  cod_sub_sector_ec in lista_subsectores["codigos"]:
                lt.addLast(lista_subsectores["codigos"][cod_sub_sector_ec], actividad)
          
            else:
                lista_subsectores["codigos"][cod_sub_sector_ec] = lt.newList(datastructure='ARRAY_LIST', cmpfunction=compare)
                lt.addLast(lista_subsectores["codigos"][cod_sub_sector_ec], actividad)
          
        codigos = lista_subsectores["codigos"]
        nomina_total = 0
        dicc_año_retenciones_totales = {"data": lt.newList(datastructure='ARRAY_LIST')}
        
        for llaves in codigos:
            impuesto = codigos[llaves]["elements"]
            nomina_total  = 0
            ingr_netos_totales = 0
            total_costos_gastos = 0
            total_saldo_por_pagar = 0
            total_saldo_favor = 0
            
            for elem in impuesto:
                año = elem["Año"]
                codigo_sec_econ = elem["Código sector económico"]
                nombre_sec_econ = elem["Nombre sector económico"]
                #codigo_subsector = elem["Código subsector económico"]
                nombre_subsector = elem["Nombre subsector económico"]
                
                ingr_netos = elem["Total ingresos netos"]
                costos_y_gastos = elem["Total costos y gastos"]
                saldo_por_pagar = elem["Total saldo a pagar"]
                saldo_favor = elem["Total saldo a favor"]
                
                nomina_total_imp  = elem["Costos y gastos nómina"]
                
                nomina_impuesto = int(nomina_total_imp )
                ingr_netos_impuesto = int(ingr_netos)
                costos_y_gastos = int(costos_y_gastos)
                saldo_por_pagar = int(saldo_por_pagar)
                saldo_favor = int(saldo_favor)
                
                
                nomina_total += nomina_impuesto
                ingr_netos_totales += ingr_netos_impuesto
                total_costos_gastos += costos_y_gastos
                total_saldo_por_pagar +=  saldo_por_pagar
                total_saldo_favor += saldo_favor
                
            info = {}
            info["Año"] = año
            info["Código sector económico"] = codigo_sec_econ
            info["Nombre sector económico"] = nombre_sec_econ
            info["Código subsector económico"] = llaves
            info["Nombre subsector económico"] = nombre_subsector
            
            info["Total costos y gastos nómina"] = nomina_total_imp
            info["Total ingresos netos del subsector económico"] = ingr_netos_totales
            info["Total costos y gastos del subsector económico"] =  total_costos_gastos
            info["Total saldo por pagar del subsector económico"] = total_saldo_por_pagar
            info["Total saldo a favor del subsector económico"] = total_saldo_favor
            
            lt.addLast(dicc_año_retenciones_totales["data"],info)
            
        merg.sort(dicc_año_retenciones_totales["data"],sort_criteria_nomina)
        menor_por_año = lt.firstElement(dicc_año_retenciones_totales["data"])
        lt.addLast(mayores_nomina["data"], menor_por_año)
        
    merg.sort(mayores_nomina["data"],sort_criteria)
    
    return mayores_nomina

def req_3b(data_structs):
    
    lista_global  =lt.newList(datastructure='ARRAY_LIST')

    for llave_años in data_structs["Anios"]:
        lista_primeros_y_ultimos = lt.newList(datastructure='ARRAY_LIST')
        lista_años = lt.newList(datastructure='ARRAY_LIST')
        lista_por_años = data_structs["Anios"][llave_años]["elements"]
        
        for actividad in lista_por_años:
            lt.addLast(lista_años, actividad)
            
            merg.sort(lista_años, sort_criteria_retencion_AÑO)
        
        for i in range(0,3):
            actividad = lt.getElement(lista_años,1)
            lt.addLast(lista_primeros_y_ultimos, actividad)
            lt.removeFirst(lista_años)
        
        lt.addLast(lista_global, lista_primeros_y_ultimos)
        
    return lista_global

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


def req_6(data_structs, ano):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    lista_sectores = {}
    lista_sectores["data"] = lt.newList(datastructure='ARRAY_LIST')
    for element in data_structs["Anios"][ano]["elements"]:
        mayor = True
        for elemento in data_structs["Anios"][ano]["elements"]:
            if element["Código sector económico"] == elemento["Código sector económico"] and int(elemento["Total ingresos netos"]) > int(element["Total ingresos netos"]):
                    mayor = False
        if mayor:
            lt.addLast(lista_sectores["data"], element)
    return lista_sectores


def req_7(data_structs, top, ano1, ano2):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    lista_top = {}
    lista_top["Anos"] = lt.newList(datastructure='ARRAY_LIST')
    for ano in data_structs["Anios"]:
        if int(ano) >= ano1 and int(ano) <= ano2:
            lt.addLast(lista_top["Anos"], ano)
            lista_top[ano] = lt.newList(datastructure='ARRAY_LIST')
    for anio in lista_top["Anos"]["elements"]:
        for element in data_structs["Anios"][anio]["elements"]:
            menor = True
            for elemento in data_structs["Anios"][anio]["elements"]:
                while lt.size(lista_top[anio]) < top:
                    if element["Código actividad económica"] == elemento["Código sector económico"] and int(elemento["Total costos y gastos"]) < int(element["Total costos y gastos"]) and elemento not in lista_top[anio]["elements"] and element not in lista_top[anio]["elements"]:
                        menor = False
            if menor:
                lt.addLast(lista_top[anio], menor)
    return


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

def compare2(data_1, data_2, id):
    if data_1[id] < data_2[id]:
        return False
    elif data_1[id] > data_2[id]:
        return True
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
    
def cmp_impuestos_by_subsector_ec(data_1, data_2):
    subsect = compare(data_1, data_2, "Código subsector económico")
    return subsect
    
def sort_criteria_subsector_ec(data_1, data_2):
    return cmp_impuestos_by_subsector_ec(data_1, data_2)

def sort_crit_orden_retenciones(data_1, data_2):
    return cmp_impuestos_by_reteniones(data_1, data_2)

def cmp_impuestos_by_reteniones(data_1, data_2):
    retencion_mayor = compare(data_1, data_2, "Total de retenciones del subsector económico")
    return retencion_mayor

def sort_criteria_retencion(data_1, data_2):
    return cmp_impuestos_by_reteniones(data_1, data_2)

def sort_criteria_retencion_AÑO(data_1, data_2):
    return cmp_impuestos_by_retenciones_AÑO(data_1, data_2)

def cmp_impuestos_by_retenciones_AÑO(data_1, data_2):
    retencion_menor = compare(data_1, data_2, "Total retenciones")
    return retencion_menor

def cmp_impuestos_nomina(data_1,data_2):
    mayor_nomina = compare2(data_1, data_2, "Total costos y gastos nómina")
    return mayor_nomina
    
def sort_criteria_nomina(data_1,data_2):
    return cmp_impuestos_nomina(data_1,data_2)

def sort_criteria_aporte_nomina(data_1,data_2):
    return cmp_impuestos_aporte_nom(data_1,data_2)

def cmp_impuestos_aporte_nom(data_1,data_2):
    menor_aporte = compare(data_1,data_2,"Total costos y gastos nómina")
    return menor_aporte