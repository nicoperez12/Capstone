## Readme simulacion hospital

El archivo **main4.py** es donde se realiza la simulación. 

Se espera optimizar la dotacion de personal extra en cada mes a través de una simulación. Esa es la variable a optimizar.

Los parametros varían en cada mes asi que el resultado no es ni constante en cada mes ni deterministico.

El archivo **parametros.py** contiene un diccionario de parametros.
Esperamos hacer este archivo escalable para que pueda contener datos de todo el año y su modificación sea facil y rapida.

Por el momento la simulación asume que la política es:
-Falta alguien. Se busca hora extra. Si no se busca personal extra. Si no rip. Nos gustaría saber cual es la cantidad de personal extra que evita la muerte (considerando que la multa es millonaria)

Queda por implementar el ausentismo como variable aleatoria. Si alguien falta, va a faltar 3 días. Hay que hacer que eso sea más aleatorio aún y que se adapte a los datos. 

El archivo **funciones.py** contiene muchas funciones que permiten el funcionamiento interno de la simulación. 

Con los comentarios de cada archivo más la lectura del primer informe debiese quedar claro cada aspecto incorporado hasta ahora en el código. Teniendo eso en mente queda por implementar:

- Variabilidad de los datos con cada mes
- Discretizacion y aleatorizacion del ausentismo
- Incorporación de vacaciones y prenatales/post natales
- Optimizacion en optuna/programa afin.
- Pulir aspectos del código que no hayan quedado claros
- Crear dumps que permitan un analisis grafico y estadístico
- Hacer análisis de sensibilidad (probablemente sobre las variables aleatorias para dar robustez a las soluciones)

Para ver los resultados de lo que se lleva se puede correr el archivo **main4.py**
Actualizacion:
Se recomienda fuertemente comentar los prints de **main4.py** y correr **sim_optuna.py** en su lugar.
