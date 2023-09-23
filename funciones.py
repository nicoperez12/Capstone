import calendar
import numpy as np

# Aqui hacer la implementacion de Seba
# Función para generar la tabla de programación inicial
def generador_tablas(dias, ratio):
    tabla = np.zeros((ratio, dias), dtype=object)
    config_inicial = ["D", "N", "L", "L"]
    config_total = config_inicial * (ratio // len(config_inicial)) + config_inicial[:ratio % len(config_inicial)]
    for dia in range(dias):
        for i in range(ratio):
            tabla[i, dia] = config_total[i]
        config_total = [config_total[-1]] + config_total[:-1]
    return tabla

def imprimir_planilla(planilla):
    for i, fila in enumerate(planilla):
        print(f"Enfermera {i}: {' | '.join(fila)}")

def generar_planilla_horas_extras(tabla):
    dias = len(tabla[0])
    enfermeras = len(tabla)
    # Inicializar la planilla de horas extras como una matriz de ceros
    planilla_horas_extras = [[0 for _ in range(dias)] for _ in range(enfermeras)]

    return planilla_horas_extras

def imprimir_planilla_horas_extras(planilla_horas_extras):
    for i, fila in enumerate(planilla_horas_extras):
        print(f"extra_{i + 1}: {' | '.join(map(str, fila))}")

# Ejemplo de uso
""" enfermeras = 5
dias = 7 """

# Generar la tabla de turnos original
""" tabla_turnos_generada = generador_tablas(parametros["dias"], parametros["ratio"])
imprimir_planilla(tabla_turnos_generada) """

# Generar la planilla de horas extras basada en la tabla de turnos original
""" planilla_horas_extras_generada = generar_planilla_horas_extras(tabla_turnos_generada)
imprimir_planilla_horas_extras(planilla_horas_extras_generada) """

# Función identificadora de semana:
def identificar_semana_y_dias(mes, dia):
    # Obtener el número de días en el mes
    num_dias = calendar.monthrange(2023, mes)[1]

    # Validar que el día proporcionado esté dentro del rango del mes
    if dia < 1 or dia > num_dias:
        return "El día no está dentro del rango del mes."

    # Obtener el día de la semana para el primer día del mes
    primer_dia_mes = calendar.weekday(2023, mes, 1)

    # Obtener el número de la semana para el día proporcionado
    semana = (dia + primer_dia_mes - 1) // 7 + 1

    # Calcular los días que pertenecen a esa semana
    primer_dia_semana = (semana - 1) * 7 - primer_dia_mes + 2
    ultimo_dia_semana = min(primer_dia_semana + 6, num_dias)
    return primer_dia_semana, ultimo_dia_semana
""" 
    print(f"El día {dia} de {calendar.month_name[mes]} pertenece a la semana {semana}.\
            Los días de esa semana son del {primer_dia_semana} al {ultimo_dia_semana}.") """

# Ejemplo de uso
""" mes = 9  # Septiembre
dia = 21  # Día a identificar
resultado = identificar_semana_y_dias(mes, dia)
print(resultado) """

# Esta funciion genera una cantidad de personal extra en base a una tabla 
def generar_tabla_personal_extra(tabla_referencia, cantidad):
    dias = len(tabla_referencia[0])
    # Inicializar la tabla de personal extra con 0's y nombre i de cantidad
    tabla_personal_extra = [['0' for _ in range(dias)] for _ in range(cantidad)]
    return tabla_personal_extra

def imprimir_tabla_personal_extra(planilla_horas_extras):
    for i, fila in enumerate(planilla_horas_extras):
        print(f"p_extra_{i}: {' | '.join(map(str, fila))}")


# Ejemplo de uso para generar una tabla de 5 filas y 7 columnas
""" filas = 5
columnas = 7
tabla_personal_extra = generar_tabla_personal_extra(tabla_turnos_generada, 4)
imprimir_tabla_personal_extra(tabla_personal_extra)
 """

# Esta funcion busca implementar un turno extra
# Se le da una tabla original, una tabla de turnos extras, y busca algun espacio en el dia específico que satisfaga las restricciones
def implementar_turnos_extras(tabla_original, tabla_turnos_extra, tipo, dia):
    # Se debe satisfacer la persona solo puede hacer turno extra si es que su celda lo permite (L)
    # Además no puede permitirse un N D o un D N en esa "vecindad"
    # El primero que encuentre va
    # Debe satisfacer que en la semana no haya hecho más de 1 
    for i in range(len(tabla_original)): #recorre el indice de enfermeras
        if tabla_original[i][dia] == "L" : # Candidatea por la primera condición
            if revisar_vecindad(tabla_original, tipo, i, dia):
                if revisar_semana(tabla_turnos_extra, i, dia):
                    tabla_turnos_extra[i][dia] = tipo
                    print(f"la enfermera {i} debiese hacer un turno extra el dia {dia} de tipo {tipo}")
                    return tabla_turnos_extra
                
    print(f"No hay turnos extra disponibles!")
    return tabla_turnos_extra
    # Aqui en la simulacion debiese partir la de buscar personal extra!

def implementar_personal_extra(tabla_personal_extra, tipo, dia):
    # Acá busca si hay algun personal extra:
    for i in range(len(tabla_personal_extra)):
        # Verificar el primero que cumpla la condición
        if tabla_personal_extra[i][dia] == "0":
            if revisar_vecindad(tabla_personal_extra, tipo, i, dia):
                tabla_personal_extra[i][dia] == tipo
                return tabla_personal_extra
    print("No hay personal extra disponible! Alta multa!")
    return tabla_personal_extra

                
#Esto aplica para cuando hay horas extras:                
def revisar_vecindad(tabla_original, tipo, i, dia):
    #Esta función revisa los días adyacentes pa que no se trabajen 24 horas seguidas.
    # No se puede permitir una situación del tipo N D    
    try:
        if tipo == "N":
            if tabla_original[i][dia+1] == "D":
                return False
        else:
            return True
    except:
        return True
    
def revisar_semana(tabla_turnos_extra, i, dia):
    # Esto revisa si una enfermera i puede hacer un turno extra o no
    # Esto esta harcodeado, hay que implementarlo bien (añadir argumento de mes)
    # Pero por mientras va a servir
    mes = 9 
    try:
        primer_dia_semana, ultimo_dia_semana = identificar_semana_y_dias(mes, dia)
    except ValueError:
        print("Esos días no corresponden al mes")
        return False
    # Contar para esa fila en especifico si los días en la semana ya tienen un D o N 
    tabla_turnos_extra_np = np.array(tabla_turnos_extra)[i, primer_dia_semana:ultimo_dia_semana]
    count_of_N = np.count_nonzero(tabla_turnos_extra_np == 'N')  # Count "N" values in the column
    count_of_D = np.count_nonzero(tabla_turnos_extra_np == 'D')
    if count_of_D + count_of_N > 1:
        return False
    else:
        return True

# Esto lo hizo seba:   
# Función para contar ausencias
# Servirá para generar estadísticas 
def contar_ausencias(tabla):
    # Cris: esto funciona con una tabla hecha como array en numpy vdd?
    # no como una lista de listas de python vdd?
    return np.sum(tabla == 'A')

# Esto lo hizo seba:
def calcular_costos(tabla, tabla_horas_extra, parametros):
    # Obtener el número de ausencias
    #Cris: Esta linea esta escrita pero según el IDLE no se usa! Revisar**
    num_ausencias = contar_ausencias(tabla)
    
    # Obtener el número de horas extra
    num_horas_extra = np.sum(tabla_horas_extra == 'D') + np.sum(tabla_horas_extra == 'N')
    
    # Obtener los costos a partir de los parámetros
    costo_ausencia = parametros['infactibilidad']  # Costo de no tener suficiente personal
    # Cris: Ojo que debiese implementarse el costo de infactibilidad!!!
    costo_hora_extra = parametros['costo_hora_extra']  # Costo de hora extra
    
    # Calcular el costo total
    costo_total = num_horas_extra * costo_hora_extra + num_ausencias * costo_ausencia 
    
    return costo_total


def calcular_estadisticas(tabla, tabla_horas_extra):
    total_ausencias = sum(cell == 'A' for row in tabla for cell in row)
    total_horas_extra = sum(cell == 'D' for row in tabla_horas_extra for cell in row) + sum(cell == 'N' for row in tabla_horas_extra for cell in row)

    return {
        'total_ausencias': total_ausencias,
        'total_horas_extra': total_horas_extra
    }
