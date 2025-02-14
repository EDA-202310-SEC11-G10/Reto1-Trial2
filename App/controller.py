﻿"""
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
 """

import config as cf
import model
import time
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def new_controller():
    """
    Crea una instancia del modelo
    """
    control = model.new_data_structs()
    return control


# Funciones para la carga de datos

def load_data(control, filename):
    """
    Carga los datos del reto
    """
    file = cf.data_dir + "DIAN/Salida_agregados_renta_juridicos_AG-"+ filename
    input_file = csv.DictReader(open(file, encoding="utf-8"))
    
    for impuesto in input_file:
        model.add_data(control, impuesto)
  
    return control

# Funciones de ordenamiento

def sort(control):
    """
    Ordena los datos del modelo
    """
    datos = model.sort(control)
    return datos


# Funciones de consulta sobre el catálogo

def get_data(control, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Llamar la función del modelo para obtener un dato
    pass

def data_size(control):
    filas = model.data_size(control)
    return filas

def req_1(control):
    """
    Retorna el resultado del requerimiento 1
    """
    impuestos_org_total_saldo_pagar = model.req_1(control) 
    return impuestos_org_total_saldo_pagar


def req_2(control):
    """
    Retorna el resultado del requerimiento 2
    """
    subsectores_menores_retenciones = model.req_2(control)
    return subsectores_menores_retenciones

def req_2b(control):
    parte2 = model.req_2b(control)
    return parte2
    
def req_3(control):
    """
    Retorna el resultado del requerimiento 3
    """
    nomina = model.req_3(control)
    return nomina

def req_3b(control):
    parte2 = model.req_3b(control)
    return parte2
    
def req_4(control):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(control):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(control, ano):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    return model.req_6(control, ano)


def req_7(control, top, ano1, ano2):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    return model.req_7(control, top, ano1, ano2)


def req_8(control):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed
