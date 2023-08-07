# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 19:39:30 2023

@author: Anber
"""

from typing import Dict, Tuple, Union
from datetime import datetime
import re
import os

def procesar_datos(nombreArchivo: str) -> Dict[str, Dict]:
    
    diccionario_observaciones = {} 
    diccionario_predicciones = {} 
    
    lista_observaciones_corruptas = []  
    lista_predicciones_corruptas = [] 
    
    registro_FechasHoras_observaciones = set() # Conjunto en el que se registran las variables FechaHora no repetidas en las observaciones
    registro_FechasHoras_predicciones = set()  # Lo mismo pero con las predicciones
    
    def parsear_fecha(fecha: str, hora: str) -> datetime:
        separador = r'[.:\/-]'
        fecha_formateada = re.sub(separador, '-', fecha)
        hora_formateada = re.sub(separador, ':', hora)
        fecha_hora_formateada = fecha_formateada + ' ' + hora_formateada
        try:
            return datetime.strptime(fecha_hora_formateada, "%Y-%m-%d %H:%M")
        except ValueError:
            pass #Aquí podría poner un aviso tipo raise ValueError(f"Fecha o hora no válidas: {fecha_hora_formateada}")
        
    def parsear_linea (linea: list) -> Tuple[datetime, Union[float, Tuple[float, int]]]:
        if len(linea) == 4:
            FechaHora = parsear_fecha(linea[0], linea[1])
            valor = (float(linea[3]), int(linea[2]))
        elif len(linea) == 3:
            FechaHora = parsear_fecha(linea[0], linea[1])
            valor = float(linea[2])
            
        return FechaHora, valor
     
    
    try:
        with open(nombreArchivo, 'r') as datos_muestra, open(os.path.join(os.path.dirname(nombreArchivo), 'Entradas_Corruptas'), 'w') as datos_corruptos:
            
            for linea in datos_muestra:
                linea = linea.strip()
                
                if not linea:
                    continue
                
                lista_linea= linea.split()
                
                if linea.lower().startswith('observaciones'):
                    marcador = True
                    
                elif linea.lower().startswith('predicciones'):
                    marcador = False
                    
                elif marcador:
                    try:
                        FechaHora, (velocidad, produccion) = parsear_linea(lista_linea)
                        if FechaHora not in registro_FechasHoras_observaciones:
                            diccionario_observaciones[FechaHora] = (velocidad,  produccion)
                            registro_FechasHoras_observaciones.add(FechaHora)       
                        else:
                            if FechaHora in diccionario_observaciones:
                                lista_observaciones_corruptas.append(f"{FechaHora} {diccionario_observaciones[FechaHora][0]} {diccionario_observaciones[FechaHora][1]} (fecha y hora repetidas)\n")
                                lista_observaciones_corruptas.append(linea + ' (fecha y hora repetidas)\n')
                                del diccionario_observaciones[FechaHora]
                            else:
                                lista_observaciones_corruptas.append(linea + ' (fecha y hora repetidas)\n')

                    except (ValueError, IndexError):            
                        lista_observaciones_corruptas.append(linea + '\n')
                        pass
                        
                elif marcador == False: 
                    try:
                        FechaHora, velocidad = parsear_linea(lista_linea)
                        if FechaHora not in registro_FechasHoras_predicciones:
                            diccionario_predicciones[FechaHora] = velocidad
                            registro_FechasHoras_predicciones.add(FechaHora)       
                        else:
                            if FechaHora in diccionario_predicciones:
                                lista_predicciones_corruptas.append(f"{FechaHora} {diccionario_predicciones[FechaHora]} (fecha y hora repetidas)\n") 
                                lista_predicciones_corruptas.append(linea + ' (fecha y hora repetidas)\n')
                                del diccionario_predicciones[FechaHora]
                            else:
                                lista_predicciones_corruptas.append(linea + ' (fecha y hora repetidas)\n')
                   
                    except (ValueError, IndexError):
                            lista_predicciones_corruptas.append(linea + '\n')
                            pass
                        
            datos_corruptos.write('Observaciones corruptas\n' + ''.join(lista_observaciones_corruptas))
            datos_corruptos.write('\nPredicciones corruptas\n' + ''.join(lista_predicciones_corruptas))
    except:
        print("Algo ha pasado, revisa el archivo de entrada \n")        
    
    return {'observaciones': diccionario_observaciones, 'predicciones': diccionario_predicciones}






