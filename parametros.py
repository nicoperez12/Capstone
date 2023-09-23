parametros = {'num_columnas' :10, 'num_filas':5 , "ratio": 1,
               "tamaño": 10, "dias" : 30, 
               "costo_hora_extra": 1000,
               'costo_personal_extra': 100,
               'infactibilidad': 10**10,
               'alpha' : 3,
               'beta': 28,
               'bernoulli': 0.8}


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