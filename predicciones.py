# -*- coding: utf-8 -*-

from typing import Dict, Tuple, List
from datetime import datetime

def resultados(predicciones: Dict, betas: Tuple[float, float]) -> Dict:
    beta0, beta1 = betas
    previsionesDict = {}
    for FechaHora, velocidad in predicciones.items():
        previsionesDict[FechaHora] = int(beta0 + beta1*velocidad)
    
    return previsionesDict

def resultados_ordenados(previsiones: Dict) -> List[Tuple[str, int]]:
    FechasHoras = previsiones.keys()
    FechasHoras_ordenadas = sorted(FechasHoras, key=lambda x: datetime.strptime(str(x), '%Y-%m-%d %H:%M'))
    
    ListaFinal = zip(FechasHoras_ordenadas, previsiones.values())
    
    for FechaHora, prevision in ListaFinal:
        print(f'{FechaHora} {round(prevision, 2)}')

