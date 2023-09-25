parametros = {'num_columnas' :10, 'num_filas':5 , "num_enfermeras": 651,
               "min_enfermeras": 91,
               "tamaño": 10, "dias" : 30, 
               "costo_hora": 1,
               "costo_hora_extra_dia": 1.25,
               "costo_hora_extra_noche": 1.5,
               'costo_personal_extra': 0.075,
               'infactibilidad': 10**10,
               'bernoulli': 0.20621762}

alpha_meses = {1: 3.623318,
               2: 2.967290,
               3: 3.477987,
               4: 3.322314,
               5: 3.500824,
               6: 3.410596,
               7: 3.589316,
               8: 4.023923,
               9: 3.837580,
               10: 4.325243,
               11: 3.908953,
               12: 4.150072}


# Notas sobre el funcionamiento de Beta y como hacer el código más escalable:
""" Given alpha and β, you can calculate the probability that a nurse will be absent on any given
day using the Beta distribution's probability density function (PDF).
For example, if you have alpha = 5 and β = 20, it suggests that, on average, the nurse is
 absent approximately 5 out of (5 + 20) = 25 days.
 """

# Los parametros son escalables por mes:
#      Esto modifica: dias, alpha, beta, prob_vacaciones, ratios quizás, ausentismo

# Falta implementar una probabilidad de vacaciones que se instancie al principio de cada mes.

# Implementar ratios y pulir esa parte en la generación de tablas