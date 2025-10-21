# Simulador de Asignación de Memoria y Planificación (SRTF/Best-Fit)

## 🎯 Objetivo
Implementación de un simulador de Sistemas Operativos que modela el ciclo completo de un proceso en un esquema de un solo procesador.

## ⚙️ Algoritmos y Estructuras Implementadas

1.  **Planificación de CPU:** Algoritmo **SRTF** (*Shortest Remaining Time First*) con Apropiación.
2.  **Gestión de Memoria:** Particiones Fijas (100K SO, 250K, 150K, 50K) con asignación **Best-Fit**.
3.  **Estados de Proceso:** Manejo de los 5 estados requeridos: **Nuevo, Listo, Listo/Suspendido, Ejecución, Terminado**.
4.  **Salidas:** Generación de la Tabla de Particiones (con **Fragmentación Interna**) y el Informe Estadístico Final (T. Retorno, T. Espera, Rendimiento).