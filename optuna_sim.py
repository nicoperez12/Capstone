# AQUI DEBIESE IMPLEMENTARSE LA SIMULACIÓN SEGUN LA TABLA:
from parametros import parametros 
from funciones import *
import random
import numpy as np
from main4 import *
import optuna
import optuna.visualization as ov

#Optuna
def objetivo(trial):
    # Define los hiperparámetros que Optuna debe optimizar.
    # En este caso, estamos optimizando los valores en la lista.
    lista_optimizada = [trial.suggest_int(f'costosmes{mes}', 1, 10) for mes in range(1, 13)]

    # Llama a la función de simulación del año con la lista optimizada.
    costo_anual = simular_año(lista_optimizada)

    #Queremos minimizar el costo anual.
    return costo_anual

costo_anual = simular_año(lista)
print("Costo anual: ", costo_anual)

study = False
study = optuna.create_study(direction='minimize')

if study:
    study.optimize(objetivo, n_trials=100)
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