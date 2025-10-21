"""Archivo para definir las clases"""
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Proceso:
    """
    Representa un proceso en el simulador. 
    Contiene la información de entrada y las métricas de planificación SRTF.
    NOTA: Faltarian añadir mas atributos para los calculos finales
    """
    id_proceso: int  # Identificador del proceso
    ta: int  # Tiempo de Arribo del proceso
    te: int  # Tiempo de Irrupción/Ejecución total en el CPU
    tamaño: int  # Tamaño del proceso
    # Estado Actual del Proceso(Nuevo, Listo, Listo/Suspendido, Terminado, Ejecución)
    estado: str = "-"

    # fiel(init=false) para que no se tenga que pasar como parametro
    tiempo_restante: int = field(init=False)

    def __post_init__(self):  # Se crea despues de instanciar el objeto
        """
        Inicializa el tiempo restante al valor de TE al crear el objeto.
        Este valor se va a decrementar en tiempos de ejecución
        """
        self.tiempo_restante = self.te

    def __hash__(self):
        """Permite usar el objeto Proceso en conjuntos o como clave de diccionario."""
        return hash(self.id_proceso)


@dataclass
class Particion:
    """
    Representa una de las particiones fijas de la memoria principal.
    Almacena el estado de la Partición y calcula automaticamente la fragmentación interna
    """
    nro_particion: int
    # Dirección de memoria donde comienza la partición (Nada importante realmente)
    dir_comienzo: int
    tamaño: int  # Tamaño fijo de la partición
    # Proceso en ejecución (None si está libre).
    proceso_en_ejec: Optional[Proceso] = None
    # La fragmentación interna se calcula al asignar un proceso, el valor inicial es 0.
    fragmentacion_interna: int = field(init=False, default=0)

    def esta_libre(self):
        """Devuelve True si la partición no tiene un Proceso almacenado"""
        return self.proceso_en_ejec is None

    def asignar_particion(self, p: Proceso):
        """
        Asigna el proceso a la partición.
        Verifica el tamaño (Aunque enrealidad antes ya se tuvo que verificar) y calcula la fragmentación interna (FI).
        """
        if self.tamaño >= p.tamaño:
            self.proceso_en_ejec = p
            self.fragmentacion_interna = self.tamaño - p.tamaño
            # NOTA: Me parece que aca ya deberia actualizar el estado del proceso a "Listo" o "Ejecución", se vera mas adelante.
        else:
            print(
                f"No se puede asignar el proceso {p.id_proceso} en la particion {self.nro_particion}")

    def liberar(self):
        """
        Libera la partición, restableciendo su estado de ocupación y fragmentación.
        Se llama cuando el proceso asignado finaliza o es desalojado de memoria.
        """
        self.proceso_en_ejec = None
        self.fragmentacion_interna = 0
