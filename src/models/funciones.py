from abc import ABC, abstractmethod

class Funcion(ABC):
    def __init__(self, codigo, titulo, duracion_min, horario, sala):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__duracion_min = duracion_min
        self.__horario = horario
        self.__sala = sala
        self._asientos_vendidos = 0
        self.__asientos_disponibles = 100
        self._recaudacion = 0

    @property
    def codigo(self):
        return self.__codigo

    @property
    def titulo(self):
        return self.__titulo

    @property
    def horario(self):
        return self.__horario

    @property
    def sala(self):
        return self.__sala

    @abstractmethod
    def calcular_precio_entrada(self):
        """
        Método abstracto para calcular el precio de entrada específico.
        Obliga a las subclases a implementar este método. (Abstracción, Polimorfismo)
        """
        pass

    @abstractmethod
    def obtener_restriccion_edad(self):
        """
        Método abstracto que devuelve la restricción de edad.
        (Abstracción, Polimorfismo)
        """
        pass

    def vender_entrada(self, cantidad):
        """
        Vende entradas si hay suficientes asientos disponibles.
        (Encapsulación, Ocultamiento de datos)
        """
        if cantidad > self.__asientos_disponibles - self._asientos_vendidos:
            print("No hay suficientes asientos disponibles")
            return False
        self._asientos_vendidos += cantidad
        self._recaudacion += cantidad * self.calcular_precio_entrada()
        return True

    def __calcular_ocupacion_porcentaje(self):
        """
        Calcula el porcentaje de ocupación basado en asientos vendidos.
        (Encapsulación, ocultamiento del método privado)
        """
        return (self._asientos_vendidos / self.__asientos_disponibles) * 100

    def get_recaudacion(self):
        """
        Devuelve la recaudación acumulada por la venta de entradas.
        """
        return self._recaudacion

class FuncionEstreno(Funcion):
    """
    Clase que representa funciones de estreno.
    Hereda de Funcion (Herencia).
    """
    def __init__(self, codigo, titulo, duracion_min, horario, sala, semana_estreno, idioma, formato_proyeccion):
        super().__init__(codigo, titulo, duracion_min, horario, sala)
        self.semana_estreno = semana_estreno
        self.idioma = idioma
        self.formato_proyeccion = formato_proyeccion

    def calcular_precio_entrada(self):
        """
        Precio fijo para funciones estreno.
        Implementación del método abstracto. (Polimorfismo)
        """
        return 10

    def obtener_restriccion_edad(self):
        """
        Restricción de edad para funciones estreno.
        """
        return "Mayores de 15"

class PeliculaClasica(Funcion):
    """
    Clase que representa películas clásicas.
    Hereda de Funcion (Herencia).
    """
    def __init__(self, codigo, titulo, duracion_min, horario, sala, anio_estreno, restaurada, precio_especial):
        super().__init__(codigo, titulo, duracion_min, horario, sala)
        self.anio_estreno = anio_estreno
        self.restaurada = restaurada
        self.precio_especial = precio_especial

    def calcular_precio_entrada(self):
        """
        Calcula precio basado en si tiene precio especial o no.
        """
        return 5 if not self.precio_especial else self.precio_especial

    def obtener_restriccion_edad(self):
        """
        Restricción de edad para películas clásicas.
        """
        return "Todo publico"

class Documental(Funcion):
    """
    Clase que representa documentales.
    """
    def __init__(self, codigo, titulo, duracion_min, horario, sala, tema, duracion_extendida, funcion_educativa):
        super().__init__(codigo, titulo, duracion_min, horario, sala)
        self.tema = tema
        self.duracion_extentida = duracion_extendida
        self.funcion_educativa = funcion_educativa

    def calcular_precio_entrada(self):
        """
        Precio fijo para documentales.
        """
        return 7

    def obtener_restriccion_edad(self):
        """
        Restricción de edad para documentales.
        """
        return "Mayores de 8"

class EventoEspecial(Funcion):
    """
    Clase que representa eventos especiales.
    """
    def __init__(self, codigo, titulo, duracion_min, horario, sala, tipo_evento, transmision_vivo, precio_premium):
        super().__init__(codigo, titulo, duracion_min, horario, sala)
        self.tipo_evento = tipo_evento
        self.transmision_vivo = transmision_vivo
        self.precio_premium = precio_premium

    def calcular_precio_entrada(self):
        """
        Precio fijo para eventos especiales.
        """
        return 15

    def obtener_restriccion_edad(self):
        """
        Restricción de edad para eventos especiales.
        """
        return "Mayores de 18"

