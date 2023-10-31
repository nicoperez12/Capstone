# AQUI DEBIESE IMPLEMENTARSE LA SIMULACIÓN SEGUN LA TABLA:
from parametros import cant_enfermeras_por_area
from funciones import *
import random
import numpy as np
from main4 import *
import optuna
import optuna.visualization as ov
from optuna.samplers import TPESampler

#Optuna
def objetivo_enfermeras(trial):
    # Define los hiperparámetros que Optuna debe optimizar.
    # En este caso, estamos optimizando los valores en la lista.
    horas_extra_optimas = []
    for mes in range(1, 13):
        horas_extra_mes = {}
        for area, cant_enfermeras in cant_enfermeras_por_area.items():
            sugerencia = trial.suggest_int(f'Horas extra mes {mes} {area}', 0, cant_enfermeras)
            #diccionario de horas extra por mes y area
            horas_extra_mes[area] = sugerencia
        horas_extra_optimas.append(horas_extra_mes)
    
    # Llama a la función de simulación del año con la lista optimizada.
    costo_acumulado_anual = 0
    for mes in range(1, 13):
        costo_acumulado_anual += simular_mes_enfermeras(mes, horas_extra_optimas[mes-1])

    #Queremos minimizar el costo anual.
    return costo_acumulado_anual

def objetivo_tens(trial):
    # Define los hiperparámetros que Optuna debe optimizar.
    # En este caso, estamos optimizando los valores en la lista.
    horas_extra_optimas = []
    for mes in range(1, 13):
        horas_extra_mes = {}
        for area, cant_tens in cant_tens_por_area.items():
            sugerencia = trial.suggest_int(f'Horas extra mes {mes} {area}', 0, cant_tens)
            #diccionario de horas extra por mes y area
            horas_extra_mes[area] = sugerencia
        horas_extra_optimas.append(horas_extra_mes)
    
    # Llama a la función de simulación del año con la lista optimizada.
    costo_acumulado_anual = 0
    for mes in range(1, 13):
        costo_acumulado_anual += simular_mes_tens(mes, horas_extra_optimas[mes-1])

    #Queremos minimizar el costo anual.
    return costo_acumulado_anual

#costo_anual = simular_año(lista)
#print("Costo anual: ", costo_anual)

n_iter = 100
costo_e = 0
costo_t = 0
lista_e = []
lista_t = []

study = optuna.create_study(sampler=TPESampler(), direction='minimize')
for i in range(2):
    if i == 0:
        study.optimize(objetivo_enfermeras, n_trials=n_iter, n_jobs=10)

        # Obtiene los mejores hiperparámetros y su costo asociado.
        best_params = study.best_params
        best_cost  = study.best_value
        costo_e += best_cost
        lista_e = [valor for valor in best_params.values()]

        # Visualización en gráficos (creo que se necesita libreria plotly)
        #ov.plot_optimization_history(study).show(renderer="browser")
        #ov.plot_param_importances(study).show(renderer="browser") # Hay muchos más pero estos eran los más importantes
    else:
        study.optimize(objetivo_tens, n_trials=n_iter, n_jobs=10)

        # Obtiene los mejores hiperparámetros y su costo asociado.
        best_params = study.best_params
        best_cost  = study.best_value
        costo_t += best_cost
        lista_t = [valor for valor in best_params.values()]

        # Visualización en gráficos (creo que se necesita libreria plotly)
        #ov.plot_optimization_history(study).show(renderer="browser")

print(f"\nMejores hiperparámetros encontrados ENFERMERAS\n:")
#Mejor lista de personal extra
print(f"Mejor lista encontrada: {lista_e}")
print(f"Costo mínimo encontrado: {costo_e}\n")

print("Mejores hiperparámetros encontrados TENS\n:")
#Mejor lista de personal extra
print(f"Mejor lista encontrada: {lista_t}")
print(f"Costo mínimo encontrado: {costo_t}\n")

print(f"COSTO TOTAL: {costo_e+costo_t}")