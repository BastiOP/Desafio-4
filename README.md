# README Desafio 4
~~~
CAMILO ACEVEDO ÁLVAREZ
RODRIGO MORALES PEÑA
BASTIÁN ROLDÁN PULGAR
~~~

Link al video: https://drive.google.com/file/d/11TKUNUsmE0E2s8ICalx7pb9cDPkd01V-/view?usp=sharing

## Instrucciones. 

1. Tener instalado compilador para correr python. (https://www.python.org/downloads/)
2. Abrir archivo .py desde Visual Studio Code.
3. Presionar el simbolo de Run Code en la parte superior derecha.

## Explicacion del algoritmo

El algoritmo se desarrolló en python, lenguaje mucho más sencillo para trabajar, nos permite construir la red como un grafo, teniendo como nodos las distintas neuronas del perceptrón multicapa. Se crearon dos grandes clases, la más básica es la de una neurona, la cual contiene su valor, el delta que será utilizado en el cálculo del nuevo peso y la conexión con las neuronas de la capa siguiente y la capa anterior, así como también los pesos relacionados con cada una de las neuronas de la capa anterior. La otra clase implementada será la red, la cual solo posee las capas de entrada, las capas ocultas y la de salida. Todas las estructuras de objetos serán listas, entre ellas las neuronas previas y posteriores a una neurona, sus pesos y todas las capas de la red.

En la clase neurona se pueden encontrar métodos de utilidad como la  función  de activación y su derivada, el cálculo del valor de una neurona y el cálculo de los nuevos pesos de esta. Por otro lado, en la clase red podemos encontrar las principales funciones para que el perceptrón multicapa funcione correctamente, entre ellas está la función de predicción de un resultado y la de actualización de los pesos de la red, además se tienen métodos para inicializar la red completa pero vacía, solo con los pesos correspondientes entre las neuronas.

Por último se crearon dos funciones, una que entrenara a la red y otra que se encargará de probar, ambas nos permiten ver los resultados obtenidos tras las predicciones, pero la segunda nos permite ver el porcentaje de precisión al momento de predecir.

## Coevaluación

### **Autor: Camilo Acevedo Álvarez**
\
-*Rodrigo Morales Peña*-

Criterio | Evaluación
-- | --
Asistencia y puntualidad | 0
Integración | 0
Responsabilidad | 0
Contribución | 0
Resolución de conflictos | 0 
TOTAL: 0
* Aspecto positivo:  Disposición a trabajar en los momentos necesarios.
* Aspecto negativo:  Falta de comunicación.
\
-*Bastían Roldán Pulgar*-

Criterio | Evaluación
-- | --
Asistencia y puntualidad | 0
Integración | 0
Responsabilidad | 0
Contribución | 0
Resolución de conflictos | 0
TOTAL: 0
* Aspecto positivo:  Motivación por el trabajo.
* Aspecto negativo:  Poco control de la motivación.

***
### **Autor: Rodrigo Morales Peña**
\
-*Camilo Acevedo Álvarez*-

Criterio | Evaluación
-- | --
Asistencia y puntualidad | 0
Integración | 0
Responsabilidad | 0
Contribución | 0
Resolución de conflictos | 0
TOTAL: 0

* Aspecto positivo: Tiene buena disposición en ayudar a sus compañeros, tiene paciencia
* Aspecto negativo: Es muy disperso.
\
-*Bastían Roldán Pulgar*-

Criterio | Evaluación
-- | --
Asistencia y puntualidad | 0
Integración | 0
Responsabilidad | 0
Contribución | 0
Resolución de conflictos | 0
TOTAL: +0
* Aspecto positivo: Tiene buena disposición, es centrado.
* Aspecto negativo: Tiene poca paciencia.

***
### **Autor: Bastían Roldán Pulgar**
\
-*Camilo Acevedo Álvarez*-

Criterio | Evaluación
-- | --
Asistencia y puntualidad | 0
Integración | 0
Responsabilidad | 0
Contribución | 0
Resolución de conflictos | 0
TOTAL: 0
* Aspecto positivo: Veloz aprendizaje.
* Aspecto negativo: Es desordenado.
\
-*Rodrigo Morales Peña*-

Criterio | Evaluación
-- | --
Asistencia y puntualidad | 0
Integración | 0
Responsabilidad | 0
Contribución | 0
Resolución de conflictos | 0
TOTAL: 0
* Aspecto positivo:  Se esfuerza para obtener buenos resultados.
* Aspecto negativo:  Dificultad en organizar el tiempo.
