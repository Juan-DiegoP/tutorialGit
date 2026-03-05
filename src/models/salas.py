from abc import ABC, abstractmethod


class Sala(ABC):
    def __init__(self, numero_sala, capacidad, tipo_pantalla):
        """
        Inicializa la sala con número, capacidad y tipo de pantalla.
        Crea matriz de butacas cuadrada basada en capacidad. (Encapsulación)
        """
        self.__numero_sala = numero_sala
        self.__capacidad = capacidad
        self.__tipo_pantalla = tipo_pantalla

        filas = columnas = int(capacidad ** 0.5)
        self._butacas = [[0 for _ in range(columnas)] for _ in range(filas)]

        self._estado_asientos = "Disponible"

    @abstractmethod
    def calcular_recargo_sala(self):
        """
        Método abstracto para calcular recargo específico por tipo de sala.
        Obliga implementación en subclases. (Abstracción, Polimorfismo)
        """
        pass

    @abstractmethod
    def obtener_equipamiento(self):
        """
        Método abstracto que devuelve lista de equipamiento de la sala.
        (Abstracción, Polimorfismo)
        """
        pass

    def __verificar_disponibilidad(self, fila, columna):
        """
        Verifica si un asiento específico está disponible.
        Método privado para encapsular lógica interna. (Encapsulación)
        """
        return self._butacas[fila][columna] == 0

    def reservar_asiento(self, fila, columna):
        """
        Reserva un asiento específico si está disponible y en rango.
        Actualiza estado de la sala. (Encapsulación)
        """
        if not (0 <= fila < len(self._butacas) and 0 <= columna < len(self._butacas[0])):
            print("Asiento fuera de rango")
            return False
        if self.__verificar_disponibilidad(fila, columna):
            self._butacas[fila][columna] = 1
            self._estado_asientos = "Ocupado"
            return True
        else:
            print("Asiento ya reservado")
            return False


class Sala2D(Sala):
    """
    Sala estándar 2D sin recargo adicional.
    Hereda de Sala (Herencia).
    """

    def __init__(self, numero_sala, capacidad):
        """
        Inicializa sala 2D con equipamiento estándar.
        """
        super().__init__(numero_sala, capacidad, "2D")
        self.pantalla_estandar = True
        self.sonido_dolby = True

    def calcular_recargo_sala(self):
        """
        No aplica recargo para salas 2D estándar.
        Implementación polimórfica del método abstracto. (Polimorfismo)
        """
        return 0

    def obtener_equipamiento(self):
        """
        Devuelve equipamiento disponible en sala 2D.
        """
        return ["Pantalla estandar", "Sonido Dolby"]


class Sala3D(Sala):
    """
    Sala con tecnología 3D y recargo asociado.
    Hereda de Sala (Herencia).
    """

    def __init__(self, numero_sala, capacidad, recargo_3d=3):
        """
        Inicializa sala 3D con recargo configurable.
        """
        super().__init__(numero_sala, capacidad, "3D")
        self.proyector_3D = True
        self.lentes_incluidos = True
        self.recargo_3d = recargo_3d

    def calcular_recargo_sala(self):
        """
        Retorna recargo específico para tecnología 3D.
        """
        return self.recargo_3d

    def obtener_equipamiento(self):
        """
        Lista equipamiento especializado 3D.
        """
        return ["Proyector 3D", "Lentes 3D incluidos", "Sonido mejorado"]


class SalaIMAX(Sala):
    """
    Sala IMAX con pantalla gigante y sonido inmersivo.
    Hereda de Sala (Herencia).
    """

    def __init__(self, numero_sala, capacidad, recargo_imax=5):
        """
        Inicializa sala IMAX con recargo premium.
        """
        super().__init__(numero_sala, capacidad, "IMAX")
        self.pantalla_gigante = True
        self.sonido_inmerso = True
        self.recargo_imax = recargo_imax

    def calcular_recargo_sala(self):
        """
        Retorna recargo IMAX premium.
        """
        return self.recargo_imax

    def obtener_equipamiento(self):
        """
        Equipamiento exclusivo IMAX.
        """
        return ["Pantalla gigante", "Sonido inmersivo", "Proyeccion laser"]


class SalaVIP(Sala):
    """
    Sala VIP con servicios premium y butacas reclinables.
    Hereda de Sala (Herencia).
    """

    def __init__(self, numero_sala, capacidad_reducida):
        """
        Inicializa sala VIP con capacidad reducida.
        """
        super().__init__(numero_sala, capacidad_reducida, "VIP")
        self.butacas_reclinables = True
        self.servicio_mesa = True

    def calcular_recargo_sala(self):
        """
        Recargo fijo para servicios VIP.
        """
        return 8

    def obtener_equipamiento(self):
        """
        Servicios exclusivos VIP.
        """
        return ["Butacas reclinables", "Servicio a la mesa", "Ambiente exclusivo"]


