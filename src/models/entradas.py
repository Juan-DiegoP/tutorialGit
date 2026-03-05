from abc import ABC, abstractmethod
from collections import defaultdict


class Entrada(ABC):
    def __init__(self, numero_entrada, funcion, asiento, precio_base):
        """
        Inicializa entrada con datos básicos y lista de snacks vacía.
        Encapsula atributos privados para proteger información sensible. (Encapsulación)
        """
        self.__numero_entrada = numero_entrada
        self.__funcion = funcion
        self.__asiento = asiento
        self.__precio_base = precio_base
        self._snacks_incluidos = []

    @property
    def precio_base(self):
        """
        Propiedad de solo lectura para acceder al precio base.
        Controla acceso a atributo privado. (Encapsulación)
        """
        return self.__precio_base

    @precio_base.setter
    def precio_base(self, nuevo_precio):
        """
        Setter con validación para modificar precio base.
        Solo permite precios positivos. (Encapsulación)
        """
        if nuevo_precio > 0:
            self.__precio_base = nuevo_precio

    def __aplicar_descuento_dia(self, dia_semana):
        """
        Aplica descuento especial de martes (20%).
        Método privado para lógica interna de descuentos. (Encapsulación)
        """
        descuento = 0
        if dia_semana.lower() == "martes":
            descuento = 0.20
        return self.__precio_base * (1 - descuento)

    def _precio_con_descuento_dia(self, dia_semana):
        """
        Método protegido que aplica descuento por día de la semana.
        Disponible para subclases. (Encapsulación)
        """
        return self.__aplicar_descuento_dia(dia_semana)

    @abstractmethod
    def calcular_precio_final(self):
        """
        Método abstracto para calcular precio final específico por tipo de entrada.
        Obliga implementación en subclases. (Abstracción, Polimorfismo)
        """
        pass

    def validar_requisitos(self):
        """
        Valida requisitos básicos de la entrada (por defecto True).
        Sobrescrito en subclases específicas. (Polimorfismo)
        """
        return True

    def imprimir_ticket(self):
        """
        Imprime ticket con información completa de la entrada.
        """
        print("==== TICKET CINE ====")
        print(f"Numero: {self.__numero_entrada}")
        print(f"Funcion: {self.__funcion}")
        print(f"Asiento: {self.__asiento}")
        print(f"Snacks: {','.join(self._snacks_incluidos) if self._snacks_incluidos else 'Ninguno'}")
        print(f"Total a pagar: ${self.calcular_precio_final():.2f}")
        print()


class EntradaGeneral(Entrada):
    """
    Entrada general con descuentos por día y recargo nocturno.
    Hereda de Entrada (Herencia).
    """

    def __init__(self, numero_entrada, funcion, asiento, precio_base, dia_semana, horario_funcion):
        super().__init__(numero_entrada, funcion, asiento, precio_base)
        self.dia_semana = dia_semana
        self.horario_funcion = horario_funcion

    def calcular_precio_final(self):
        """
        Calcula precio con descuento de martes y recargo nocturno (>=20:00).
        Implementación polimórfica. (Polimorfismo)
        """
        precio = self._precio_con_descuento_dia(self.dia_semana)
        if self.horario_funcion >= 20:
            precio *= 1.10  # recargo 10% noche
        return precio


class EntradaInfantil(Entrada):
    """
    Entrada para niños con restricciones de edad y descuento 50%.
    Hereda de Entrada (Herencia).
    """

    def __init__(self, numero_entrada, funcion, asiento, precio_base, edad_nino, requiere_adulto=True,
                 descuento_50=0.50):
        super().__init__(numero_entrada, funcion, asiento, precio_base)
        self.edad_nino = edad_nino
        self.requiere_adulto = requiere_adulto
        self.descuento_50 = descuento_50

    def calcular_precio_final(self):
        """
        Aplica descuento fijo del 50% para entradas infantiles.
        """
        return self.precio_base * (1 - self.descuento_50)

    def validar_requisitos(self):
        """
        Valida edad del niño (menor de 12) y acompañante si es necesario.
        Sobrescribe método de clase base. (Polimorfismo)
        """
        if self.edad_nino >= 12:
            return False
        if self.edad_nino < 8 and not self.requiere_adulto:
            return False
        return True


class EntradaEstudiante(Entrada):
    """
    Entrada para estudiantes con descuento en horarios especiales.
    Hereda de Entrada (Herencia).
    """

    def __init__(self, numero_entrada, funcion, asiento, precio_base, carnet, horario_especial=False,
                 descuento_30=0.30):
        super().__init__(numero_entrada, funcion, asiento, precio_base)
        self.carnet = carnet
        self.horario_especial = horario_especial
        self.descuento_30 = descuento_30

    def calcular_precio_final(self):
        """
        Aplica 30% descuento solo en horarios especiales.
        """
        if not self.horario_especial:
            return self.precio_base
        return self.precio_base * (1 - self.descuento_30)

    def validar_requisitos(self):
        """
        Valida que el estudiante tenga carnet válido.
        """
        return bool(self.carnet)


class ComboPromo(Entrada):
    """
    Combo promocional que incluye entrada + snacks + bebida con descuento.
    Hereda de Entrada (Herencia).
    """

    def __init__(self, numero_entrada, funcion, asiento, precio_base, entrada, snacks, bebida, descuento_combo=0.15):
        super().__init__(numero_entrada, funcion, asiento, precio_base)
        self.entrada = entrada
        self._snacks_incluidos = snacks
        self.bebida = bebida
        self.descuento_combo = descuento_combo

    def calcular_precio_final(self):
        """
        Calcula precio total del combo con 15% descuento sobre subtotal.
        """
        subtotal = self.entrada.calcular_precio_final() + self.precio_base
        return subtotal * (1 - self.descuento_combo)


