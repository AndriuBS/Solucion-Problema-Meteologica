# -*- coding: utf-8 -*-
"""
Bloque programa principal
"""

from depuracion import procesar_datos
from errores import emaYecm
from regresion import betasRegresion
from predicciones import resultados, resultados_ordenados
# from correlacion import rPearson 
# from atipicos import datosAtipicos


if __name__ == '__main__':
    
    datos = procesar_datos('datos_prueba.txt')
    
    diccionario_observaciones = datos['observaciones']
    
    """for clave, valor in diccionario_observaciones.items():
        print(f'{clave}  {valor}')

 
   diccionario_mejorado = datosAtipicos(diccionario_observaciones)
    #print(diccionario_mejorado)

    #coeficienteRPearson = rPearson(diccionario_observaciones) """


    betas = betasRegresion(diccionario_observaciones)
    beta0, beta1 = betas
    print(f'{round(beta1, 2)} {round(beta0, 2)}')

    errores = emaYecm(diccionario_observaciones, betas)
    emaDict = errores['EMA'] 
    ecmDict = errores['ECM']

    for trimestre in emaDict:
        print(f'Trimestre{trimestre} {round(emaDict[trimestre],2)} {round(ecmDict[trimestre],2)}')


    diccionario_predicciones = datos['predicciones']
    
    nuevaPrediccion = resultados(diccionario_predicciones, betas)
    nuevaPrediccionOrdenada = resultados_ordenados(nuevaPrediccion)

