# Solucion Problema Meteologica

A partir de un archivo de texto de tipo csv de observaciones y predicciones en formato:
    Observaciones
    YYYY:mm:DD HH:MM produccion velocidad
    ...
    YYYY:mm:DD HH:MM produccion velocidad
    Predicciones
    YYYY:mm:DD HH:MM velocidad
    ...
    YYYY:mm:DD HH:MM velocidad

    Teniendo en cuenta que la velocidad se considera una variable independiente a partir de la cual se infiere la producción, ambas en formato float redondeadas a 
    dos decimales, se nos pide hacer una regresión sobre los datos correspondientes a las observaciones y calcular los coeficientes beta0 y beta1, correspondientes 
    a la recta de regresión Y = beta0 + beta1 * X, y mostrarlos por pantalla.
                                                                      beta0 beta1

    A continuación se nos pide hallar los errores cuadrático medio (ECM) y medio absoluto (EMA) de cada trimestre y mostrarlos por pantalla.
                                                                  Trimestre1 ECM EMA
                                                                  Trimestre2 ECM EMA
                                                                  Trimestre3 ECM EMA
                                                                  Trimestre4 ECM EMA
    Por último, a partir de la regresión anterior, se nos pide mostrar por pantalla las predicciones ordenadas de la producción:
                                                                  Predicciones
                                                                  YYYY:mm:DD HH:MM velocidad produccion
    Notar que:
                Producción_i = beta0 + beta1 * Velocidad_i
                                                                

                                                                
