﻿"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
assert cf
from tabulate import tabulate as tab
import traceback

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_controller():
    """
        Se crea una instancia del controlador
    """
    control = controller.new_controller()
    return control


def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2 - que realmente es el 3")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8")
    print("0- Salir")

def print_opciones_carga():
    print()
    print("1. Small")
    print("2. 5%")
    print("3. 10%")
    print("4. 20%")
    print("5. 30%")
    print("6. 50%")
    print("7. 80%")
    print("8. Large")
    
def load_data(control):
    """
    Carga los datos
    """
    print_opciones_carga()
    size = int(input("Elija el tamaño del archivo: \n"))
    print("Cargando información de los archivos ....\n")
    files=["small.csv","5pct.csv","10pct.csv","20pct.csv","30pct.csv","50pct.csv","80pct.csv", "large.csv"]
    data = controller.load_data(control,files[size-1])
    controller.sort(control)
    return data


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_tabla_carga_datos(control,filas):
    carga = {"Año":[], "Código actividad económica":[], "Nombre actividad económica":[], "Código sector económico":[],
                         "Nombre sector económico":[], "Código subsector económico":[], "Nombre subsector económico":[],
                         "Total ingresos netos":[], "Total costos y gastos":[], "Total saldo a pagar":[], "Total saldo a favor":[]}

    for fila in [0,1,2,filas-3,filas-2,filas-1]:
        for llave in carga:
            carga[llave].append(control['data']['elements'][fila][llave])
    tabla = tab(carga, tablefmt='grid', headers='keys', colalign=['right','right','left','right','left','right','left','left','left','left','left'], maxcolwidths=[7,10,20,10,20,15,20,10,10,10,15], maxheadercolwidths=[7,10,20,10,20,15,20,10,10,10,15])
    print(tabla)

def print_tabla_req_1(control,filas):
    carga = {"Año":[], "Código actividad económica":[], "Nombre actividad económica":[], "Código sector económico":[],
                         "Nombre sector económico":[], "Código subsector económico":[], "Nombre subsector económico":[],
                         "Total ingresos netos":[], "Total costos y gastos":[], "Total saldo a pagar":[], "Total saldo a favor":[]}

    for fila in range(0,filas-1):
        for llave in carga:
            carga[llave].append(control['data']['elements'][fila][llave])
    tabla = tab(carga, tablefmt='grid', headers='keys', colalign=['right','right','left','right','left','right','left','left','left','left','left'], maxcolwidths=[7,10,20,10,20,15,20,10,10,10,15], maxheadercolwidths=[7,10,20,10,20,15,20,10,10,10,15])
    print(tabla)
    
def print_tabla_req_2(control,filas):
    carga = {"Año":[], "Código sector económico":[], "Nombre sector económico":[], "Código subsector económico":[], 
             "Nombre subsector económico":[], "Total de retenciones del subsector económico":[], "Total ingresos netos del subsector económico":[], 
             "Total costos y gastos del subsector económico":[], "Total saldo por pagar del subsector económico":[], 
             "Total saldo a favor del subsector económico": []}
    
    for fila in range(0,filas-1):
        for llave in carga:
            carga[llave].append(control['data']['elements'][fila][llave])
    tabla = tab(carga, tablefmt='grid', headers='keys', colalign=['right','right','left','right','left','right','left','left','left','left'], maxcolwidths=[7,10,20,10,20,15,20,10,10,10], maxheadercolwidths=[7,10,20,10,20,15,20,10,10,10])
    print("Subsectores económicos con las menores retenciones de cada año:")
    print(tabla)
    
def print_tabla_req_2b(control,año):
    carga = {"Código actividad económica":[], "Nombre actividad económica":[], "Total retenciones":[], "Total ingresos netos":[], 
             "Total costos y gastos":[], "Total saldo a pagar":[], "Total saldo a favor": []}
    
    for fila in range(0,3):
        for llave in carga:
            carga[llave].append(control[fila][llave])
    tabla = tab(carga, tablefmt='grid', headers='keys', colalign=['right','right','left','right','left','right','left'], maxcolwidths=[15,25,20,10,20,15,20], maxheadercolwidths=[15,25,20,10,20,15,20])
    print("Tres actvidades que menos aportaron al valor total de retenciones en " + año)
    print(tabla)
    
def print_tabla_2c(datos):
    for x in datos["elements"]:
        i  = 0
        lista_años = x["elements"]
        año = lista_años[i]["Año"]
        print_tabla_req_2b(lista_años,año)
        i += 1
    
def print_tabla_req3(control,filas):
    carga = {"Año":[], "Código sector económico":[], "Nombre sector económico":[], "Código subsector económico":[], 
             "Nombre subsector económico":[], "Total costos y gastos nómina":[], "Total ingresos netos del subsector económico":[], 
             "Total costos y gastos del subsector económico":[], "Total saldo por pagar del subsector económico":[], 
             "Total saldo a favor del subsector económico": []}
    
    for fila in range(0,filas-1):
        for llave in carga:
            carga[llave].append(control['data']['elements'][fila][llave])
    tabla = tab(carga, tablefmt='grid', headers='keys', colalign=['right','right','left','right','left','right','left','left','left','left'], maxcolwidths=[7,10,20,10,20,15,20,10,10,10], maxheadercolwidths=[7,10,20,10,20,15,20,10,10,10])
    print("Subsectores económicos con los mayores costos y gastos de nómina de cada año:")
    print(tabla)
    
def print_tabla_req_3b(control,año):
    carga = {"Código actividad económica":[], "Nombre actividad económica":[], "Costos y gastos nómina":[], "Total ingresos netos":[], 
             "Total costos y gastos":[], "Total saldo a pagar":[], "Total saldo a favor": []}
    
    for fila in range(0,3):
        for llave in carga:
            carga[llave].append(control[fila][llave])
    tabla = tab(carga, tablefmt='grid', headers='keys', colalign=['right','right','left','right','left','right','left'], maxcolwidths=[15,25,20,10,20,15,20], maxheadercolwidths=[15,25,20,10,20,15,20])
    print("Tres actvidades que menos aportaron al valor total de costos y gastos de nómina " + año)
    print(tabla)
    
def print_tabla_req_3c(datos):
    for x in datos["elements"]:
        i  = 0
        lista_años = x["elements"]
        año = lista_años[i]["Año"]
        print_tabla_req_3b(lista_años,año)
        i += 1
    
def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    datos_org = controller.req_1(control)
    return  datos_org


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    subsectores_menores_retenciones= controller.req_2(control)
    return subsectores_menores_retenciones

def print_req_2b(control):
    parte2 = controller.req_2b(control)
    return parte2
    
def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    nomina = controller.req_3(control)
    return nomina

def print_req_3b(control):
    parte2 = controller.req_3b(control)
    return parte2
    

def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    pass


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    pass


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    ano = input("Digite el año desea encontrar la actividad económica con el mayor total de ingresos netos para cada sector económico: ")
    print(tab((controller.req_6(control, ano))["data"]["elements"], tablefmt='grid', headers='keys', colalign=['right','right','left','right','left','right','left','left','left','left','left'], maxcolwidths=[7,10,15,10,15,15,15,10,10,10,10], maxheadercolwidths=[7,10,15,10,15,15,15,10,10,10,10]))


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    top = int(input("Digite la cantidad de impuestos para el TOP: "))
    ano1 = int(input("Digite el año de comienzo: "))
    ano2 = int(input("Digite el año de finalización: "))
    print(controller.req_7(control, top, ano1, ano2))


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass


# Se crea el controlador asociado a la vista
control = new_controller()

# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        try:
            if int(inputs) == 1:
                load_data(control)
                filas = controller.data_size(control)
                print_tabla_carga_datos(control,filas)
                
            elif int(inputs) == 2:
                datos = print_req_1(control)
                filas = controller.data_size(datos)
                print_tabla_req_1(datos,filas)

            elif int(inputs) == 3:
                subsec_menores_ret = print_req_2(control)
                filas1 = controller.data_size(subsec_menores_ret)
                print_tabla_req_2(subsec_menores_ret,filas1)
                
                datos = print_req_2b(control)
                print_tabla_2c(datos)

            elif int(inputs) == 4:
                costos_gastos_nomina = print_req_3(control)
                filas1 = controller.data_size(costos_gastos_nomina)
                print_tabla_req3(costos_gastos_nomina,filas1)
                
                datos = print_req_3b(control)
                print_tabla_req_3c(datos)

            elif int(inputs) == 5:
                print_req_4(control)

            elif int(inputs) == 6:
                print_req_5(control)

            elif int(inputs) == 7:
                print_req_6(control)

            elif int(inputs) == 8:
                print_req_7(control)

            elif int(inputs) == 9:
                print_req_8(control)

            elif int(inputs) == 0:
                working = False
                print("\nGracias por utilizar el programa")
                
            else:
                print("Opción errónea, vuelva a elegir.\n")
        except Exception as exp:
            print("ERR:", exp)
            traceback.print_exc()
    sys.exit(0)