"""
Módulo principal de ejecución del Simulador (Incompleto obviamente)
Implementa el control de tiempo y gestiona las transiciones 
de estado de los procesos entre las colas (Nuevos, Listos, Listos/Suspendidos), 
siguiendo el diagrama de flujo
"""
from rich.console import Console
from rich.table import Table
from carga_de_procesos import cargar_procesos
from clases import Proceso, Particion
from typing import Optional


def simular_os():
    """
    Inicializa el sistema (particiones, colas) y ejecuta el bucle de simulación 
    de tiempo discreto
    La función gestiona las cuatro fases del flujo del proceso en cada 
    instante: Admisión, Asignación de Memoria (BEST-FIT), Planificación (SRTF) y 
    Ejecución/Finalización.
    Todo en def para despues implementar el front (Interfaz grafica) de manera comoda
    """
    # Inicialización de la consola para la salida gráfica
    console = Console()
    # --- 1. CARGA INICIAL DE PROCESOS ---
    procesos = cargar_procesos()
    # Validación y manejo de errores (si la carga falló por alguna razon)
    if not procesos:
        console.print("[red bold]ERROR:[/red bold] No se cargo ningun proceso")
        console.input("Presione Enter para salir del programa")
        exit()
    # --- 2. INICIALIZACIÓN DE MEMORIA (Particiones Fijas) ---
    memoria = [
        # Partición 0: Sistema Operativo (no asignable)
        Particion(nro_particion=0, dir_comienzo=0, tamaño=100),
        Particion(nro_particion=1, dir_comienzo=100, tamaño=250),
        Particion(nro_particion=2, dir_comienzo=350, tamaño=150),
        Particion(nro_particion=3, dir_comienzo=500, tamaño=50)
    ]
    # Marcar la partición del SO como ocupada
    memoria[0].proceso_en_ejec = "SO"
    memoria[0].fragmentacion_interna = 0
    # --- 3. INICIALIZACIÓN DE COLAS Y VARIABLE DE TIEMPO---
    cola_nuevos = []
    cola_listos = []  # Cola de procesos listos para CPU (ya tienen memoria)
    cola_listos_suspendidos = []  # Cola de procesos en espera de asignación de memoria
    # Proceso actualmente en el procesador
    proceso_en_cpu: Optional[Proceso] = None
    instante_actual: int = 0
    # --- INICIO DE LA SIMULACIÓN ---
    console.print(
        "\n[green bold]---Inicio de la Simulación---[/green bold]\n \n", justify="center")
    input("Presione Enter para Continuar")
    while cola_nuevos or cola_listos or cola_listos_suspendidos or proceso_en_cpu:
        console.clear()
        console.rule(f"[bold yellow]Instante: {instante_actual}")
        input()
