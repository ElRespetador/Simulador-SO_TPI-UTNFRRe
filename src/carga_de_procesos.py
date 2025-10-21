"""
El modulo para la carga inicial de los procesos del simulador
Maximo 10 procesos
"""
from clases import Proceso
from rich.console import Console
from rich.table import Table


def cargar_procesos():
    """
    Gestiona la carga de procesos de forma manual o por archivo,
    creando y devolviendo una lista de objetos Proceso.
    Retorna una Lista de Objetos "Proceso" Cargados.
    """
    console = Console()
    tabla = Table()
    num_cargados = 0
    cola_procesos = []
    console.print("[green bold]CARGA DE PROCESOS[/green bold]")
    res = 0
    # -- Aca elige el usuario como quiere cargar--
    while res not in ["1", "2"]:
        res = console.input(
            "[bold]Desea cargar:\n 1_Por archivos\n 2_Manualmente\nRespuesta:[/bold]")
        if res not in ["1", "2"]:
            console.print("Respuesta invalida")
    if res == "1":
        # --Carga por archivo, despues implementamos que lo eliga desde el explorador de windows--
        with open(r"C:\Users\rodri\Visual Studio\SO\TPI 2025\proce.txt", 'r', encoding='utf-8') as archivo:
            archivo.readline()  # Se salta el encabezado del txt(ID TA TE Tamaño)
            for linea in archivo:
                datos = linea.strip().split(',')
                if len(datos) == 4:
                    try:
                        proceso = Proceso(
                            id_proceso=int(datos[0]),
                            ta=int(datos[1]),
                            te=int(datos[2]),
                            tamaño=int(datos[3])
                        )
                        cola_procesos.append(proceso)
                    except ValueError:
                        console.print(
                            f"Advertencia: Saltando línea con datos no numéricos: {linea.strip()}")
                if len(cola_procesos) == 10:  # Que corte cuando llegue a 10
                    break
    elif res == "2":
        # --Carga manualmente--
        while True:
            num_cargados += 1
            console.print("[bold]Cargue los datos del proceso[/bold]")
            try:
                proceso = Proceso(
                    id_proceso=int(input("Id del proceso: ")),
                    ta=int(input("Tiempo de Arribo: ")),
                    te=int(input("Tiempo de irrupción: ")),
                    tamaño=int(input("Ingrese el Tamaño del proceso: "))
                )
                cola_procesos.append(proceso)
            except ValueError:
                console.print(
                    "[red]Error:[/red] Ingresar solo números enteros para los parametros")
                num_cargados -= 1
                continue  # Volver a pedir datos para el mismo proceso
            if num_cargados >= 10:  # Que no sea mayor a 10
                break
            salir = console.input(
                "[magenta bold]Desea continuar? [S/N]:[/magenta bold] ")
            if salir.upper() == "N":
                break
    # Muestra de los procesos cargados
    tabla = Table(
        title="[bold cyan]Procesos Cargados en el Sistema[/bold cyan]", show_lines=True)
    tabla.add_column("ID", style="magenta bold")
    tabla.add_column("TA", style="cyan")
    tabla.add_column("TE", style="cyan")
    tabla.add_column("Tamaño", style="yellow")
    tabla.add_column("Estado Inicial", style="gray70")

    for p in cola_procesos:
        tabla.add_row(
            str(p.id_proceso),
            str(p.ta),
            str(p.te),
            str(p.tamaño),
            p.estado
        )
    console.print(tabla, justify="center")
    return cola_procesos
