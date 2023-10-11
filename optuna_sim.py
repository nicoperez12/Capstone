# AQUI DEBIESE IMPLEMENTARSE LA SIMULACIÓN SEGUN LA TABLA:
from parametros import parametros 
from funciones import *
import random
import numpy as np
from main4 import *
import optuna
import optuna.visualization as ov
from optuna.samplers import TPESampler

#Optuna
def objetivo(trial):
    # Define los hiperparámetros que Optuna debe optimizar.
    # En este caso, estamos optimizando los valores en la lista.
    lista_optimizada = [trial.suggest_int(f'Horas extra mes {mes}', 0, 100) for mes in range(1, 13)]
    
    # Llama a la función de simulación del año con la lista optimizada.
    costo_acumulado_anual = 0
    for mes in range(1, 12):
        costo_acumulado_anual += simular_mes_enfermeras(mes, lista_optimizada[mes-1])

    #Queremos minimizar el costo anual.
    return costo_acumulado_anual

#costo_anual = simular_año(lista)
#print("Costo anual: ", costo_anual)


study = optuna.create_study(sampler=TPESampler(), direction='minimize')
study.optimize(objetivo, n_trials=500, n_jobs=10)

# Obtiene los mejores hiperparámetros y su costo asociado.
best_params = study.best_params
best_cost  = study.best_value

print("Mejores hiperparámetros encontrados:")
#Mejor lista de personal extra
print(f"Mejor lista encontrada: {[valor for valor in best_params.values()]}")
print(f"Costo mínimo encontrado: {best_cost}")

# Visualización en gráficos (creo que se necesita libreria plotly)
ov.plot_optimization_history(study).show(renderer="browser")
ov.plot_param_importances(study).show(renderer="browser") # Hay muchos más pero estos eran los más importantes