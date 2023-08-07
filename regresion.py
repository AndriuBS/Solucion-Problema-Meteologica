
from typing import Dict, Tuple

def betasRegresion(observaciones: Dict[str, Dict]) -> Tuple[float, float]:
    
    n = len(observaciones)
    
    if n < 2:
       raise ValueError("Se requieren al menos 2 observaciones válidas para calcular los coeficientes de regresión.")
    
    x = [tupla[0] for tupla in observaciones.values()]  # Lista velocidades
    y = [tupla[1] for tupla in observaciones.values()]  # Lista producciones
    x_barra = sum(x) / n 
    y_barra = sum(y) / n
    Sxx = sum([(xi - x_barra) ** 2 for xi in x]) / (n - 1) 
    Syy = sum([(yi - y_barra) ** 2 for yi in y]) / (n - 1)
    Sxy = sum([(xi - x_barra) * (yi - y_barra) for xi, yi in zip(x, y)]) / (n - 1)
    beta1 = (Syy - Sxx + ((Syy - Sxx) ** 2 + 4 * Sxy ** 2) ** 0.5) / (2 * Sxy)
    beta0 = y_barra - beta1 * x_barra
    
    return beta0, beta1