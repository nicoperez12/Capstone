# AQUI DEBIESE IMPLEMENTARSE LA SIMULACIÓN SEGUN LA TABLA:
from parametros import *
from funciones import *
import random
import numpy as np
import math

# Instanciar la primera tabla
tabla1 = generador_tablas(parametros["dias"], parametros["num_enfermeras"])
tabla_horas_extra = generar_planilla_horas_extras(tabla1)
# Ese 4 es una variable. De hecho es la variable sobre la cual se optimiza
tabla_personal_extra = generar_tabla_personal_extra(tabla1, 4)
# No se sabe cuanto personal extra contratar
# El hospital rellena en forma aleatoria mientras puede (con horas extras)

# Acá debiese iniciar la simulación:
# debiese correr cada día:
# Recordar que por ahora estamos minimizando sobre la cant del personal extra:

#SIMULACION PARA ENFERMERAS

def simular_mes(mes, cant_personal_extra):
    dias = calendar.monthrange(2023, mes)[1]
    tabla1 = generador_tablas(dias, parametros["num_enfermeras"])
    tabla_horas_extra = generar_planilla_horas_extras(tabla1)
    tabla_personal_extra = generar_tabla_personal_extra(tabla1, cant_personal_extra)
    alpha = alpha_meses[mes]
    beta = dias-alpha
    #Esto se va a retornar
    costos_acumulados = 0
    # i = fila/enfermera, dia = columna
    # Este proceso revisa cada dia si la enfermera va a trabajar o no (si es que le corresponde)
    for dia in range(len(tabla1[0])):
        # Este proceso decide si la enfermera que le toca ir va o no
        for i in range(len(tabla1)):
            enfermera = tabla1[i][dia]
            if enfermera == "D" or enfermera == "N":
                if random.random() <= parametros["bernoulli"]:
                    # Aquí hay que implementar la distribución discreta para la cantidad de días
                    # Esto requiere ser modificado y pulido
                    dias_ausente = math.ceil(dias*random.betavariate(alpha, beta))
                    print(f"La enfermera de índice {i} se ha ausentado por {dias_ausente} días")
                    for j in range(0, dias_ausente):
                        try:
                        #Esto representa un ausentismo
                            tabla1[i][dia+j] = "A"
                        except:
                            continue
                else:
                    print(f"la enfermera {i} asistió al trabajo el dia {dia}" )
                    costos_acumulados += parametros["costo_hora"]*12

        # Este proceso debiese revisar que se cumplan las restricciones:
        # En particular las restricciones a llenar son que se cubra el ratio pero queda por implementar:
        # Por el momento que se satisfaga que cumpla que cada columna tenga al menos un dia y una noche 
        tabla_np = np.array(tabla1)
        # Count the number of "N" values in the third column (column index 2)
        column_to_count = tabla_np[:, dia]  # Extract the third column
        count_of_N = np.count_nonzero(column_to_count == 'N')  # Count "N" values in the column
        count_of_D = np.count_nonzero(column_to_count == 'D')
        
        if count_of_N < parametros["min_enfermeras"]:
            faltante_N = parametros["min_enfermeras"]-count_of_N
            # Aca hay que hacer algo xd, seleccionar potenciales horas extras. Implementar los algoritmos!
            if tabla_horas_extra != implementar_turnos_extras(tabla1, tabla_horas_extra, "N", dia):
                costos_acumulados += parametros["costo_hora_extra_noche"]*12*faltante_N
            else:
                if tabla_personal_extra == implementar_personal_extra(tabla_personal_extra, "N", dia):
                    costos_acumulados += parametros["infactibilidad"]
                    print(f"Hoy, día {dia} no hay suficientes enfermeras para cubrir la noche")

        if count_of_D < parametros["min_enfermeras"]:
            faltante_D = parametros["min_enfermeras"]-count_of_D
            if tabla_horas_extra != implementar_turnos_extras(tabla1, tabla_horas_extra, "D", dia):
                costos_acumulados += parametros["costo_hora_extra_dia"]*12*faltante_D
            else:
                if tabla_personal_extra == implementar_personal_extra(tabla_personal_extra, "D", dia):
                    costos_acumulados += parametros["infactibilidad"]
                    print(f"Hoy, día {dia} no hay suficientes enfermeras para cubrir el dia")

    print(calcular_estadisticas(tabla1, tabla_horas_extra))
    print(f"\nCostos acumulados de {costos_acumulados} para el mes {mes + 1}")
    return costos_acumulados

#simular_mes(1, 4)
# La lista contiene la cantidad optima de personal extra a contratar cada mes:
# Como se supone que las distribuciones son variables estas cantidades van a ser variables!
# ie: [4, 5, 6, 10, 1, 3, 6, 7]
# La optimizacion podria realizarse sobre esta funcion. 
# Analizar esto:
# Esta lista es un ejemplo!!!

lista = [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
def simular_año(lista):
    costo_acumulado_anual = 0
    for mes in range(1, 12):
        costo_acumulado_anual += simular_mes(mes, lista[mes-1])
    return costo_acumulado_anual
        
simular_año(lista)