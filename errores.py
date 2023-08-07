
from typing import Dict, Tuple

def emaYecm(observaciones: Dict[str, Dict], betas: Tuple[float, float]) -> Dict[str, Dict]:
    
    beta0, beta1 = betas
    auxDict = {} # diccionario auxiliar donde claves={1,2,3,4} y los valores son una lista de tuplas [(velcidad, produccion)] de cada trimestre
    emaDict = {}
    ecmDict = {}
    
    for FechaHora, (velocidad, produccion) in observaciones.items():
        FechaHora = str(FechaHora)
        mes = int(FechaHora.split(' ')[0].split('-')[1])
        trimestre = (mes - 1) // 3 + 1
        prediccion = beta0 + beta1*velocidad
        
        if trimestre not in auxDict:
            auxDict[trimestre] = [(produccion, prediccion)]
        else:
            auxDict[trimestre].append((produccion, prediccion))
        
    
    for trimestre, valor in auxDict.items(): # auxDict.items() = [('1', [(velocidad,tupla),...]), ('2', [(velocidad,produccion),...]), ('3', [(velocidad,produccion),...]), ('4', [(velocidad,produccion),...])]
        if len(valor) < 2: #Si hay menos de dos observaciones en un trimestre descartamos calcular los errores ya que mínimo se necesitan 2 observaciones
            emaDict[trimestre] = 'None' 
            ecmDict[trimestre] = 'None'
        else:
            emaDict[trimestre] = 100 * sum(abs(produccion - prediccion) for produccion, prediccion in valor) / sum(produccion for produccion, _ in valor)
            ecmDict[trimestre] = 100 * pow(len(valor) * sum((produccion - prediccion)**2 for produccion, prediccion in valor) , 0.5) / sum(produccion for produccion, _ in valor)                                               

    return {'EMA': emaDict, 'ECM': ecmDict}



# La variable FechaHora, que son las claves del diccionario_observaciones, es un objeto datetime, y
# al parecer un objeto datetime no permite aplicarle la función 'split', luego se me ocurre que 
# previamente he de transformar FechaHora de objeto datetime a una cadena str(FechaHora).