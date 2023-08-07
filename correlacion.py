# -*- coding: utf-8 -*-
"""
Aquí voy a ver la correlación entre las observaciones correspondientes a 
                    X - Velocidad
                    Y - Produccion energía

También puedo ver los datos más atípicos y eliminarlos de la muestra.
"""
    
from typing import Dict

def rPearson(observaciones: Dict) -> float:
    
    n = len(observaciones)
    x = [tupla[0] for tupla in observaciones.values()]  # Lista velocidades
    y = [tupla[1] for tupla in observaciones.values()]  # Lista producciones
    x_barra = sum(x) / n 
    y_barra = sum(y) / n
    Sxx = (sum([(xi - x_barra) ** 2 for xi in x])) ** 0.5   #desviación típica velocidad
    Syy = (sum([(yi - y_barra) ** 2 for yi in y])) ** 0.5   #desviación típica produccion
    Sxy = sum([(xi - x_barra) * (yi - y_barra) for xi, yi in zip(x, y)]) #Covarianza
    
    coef_r_Pearson = Sxy / (Sxx * Syy)
    
    return coef_r_Pearson