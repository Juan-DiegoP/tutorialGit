from abc import ABC, abstractmethod


class ProductoConfiteria(ABC):
    """
    Clase abstracta base para productos de confitería del cine.
    Aplica Abstracción: define interfaz común para cálculo de costos y precios.
    """
    def __init__(self, codigo, nombre, precio_base, stock, ingredientes):
        """
        Inicializa producto con datos básicos y lista de ingredientes.
        Encapsula atributos privados para proteger información crítica. (Encapsulación)
        """
        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio_base = precio_base
        self.__stock = stock
        self._ingredientes = ingredientes  # protegido

    # ================ ENCAPSULAMIENTO ================
    @property
    def codigo(self):
        """
        Propiedad de solo lectura para código del producto.
        Controla acceso a atributo privado. (Encapsulación)
        """
        return self.__codigo

    @property
    def nombre(self):
        """
        Propiedad de solo lectura para nombre del producto.
        """
        return self.__nombre

    @property
    def precio_base(self):
        """
        Propiedad de solo lectura para precio base.
        """
        return self.__precio_base

    @property
    def stock(self):
        """
        Propiedad de solo lectura para stock disponible.
        """
        return self.__stock

    def descontar_stock(self, cantidad):
        """
        Descuento de stock con validaciones de cantidad y disponibilidad.
        Método público con lógica interna protegida. (Encapsulación)
        """
        if cantidad <= 0:
            print("Cantidad inválida")
            return False
        if cantidad > self.__stock:
            print(f"No hay stock suficiente de {self.__nombre}")
            return False
        self.__stock -= cantidad
        self.__alertar_stock_bajo()
        return True

    def __alertar_stock_bajo(self):
        """
        Alerta automática cuando stock es bajo (<=5 unidades).
        Método privado para lógica interna. (Encapsulación)
        """
        if self.__stock <= 5:
            print(f"ALERTA: stock bajo de {self.__nombre} (quedan {self.__stock})")

    def __calcular_margen_ganancia(self):
        """
        Calcula margen de ganancia base del 40%.
        Método privado reutilizable. (Encapsulación)
        """
        return 0.40

    # METODOS ABSTRACTOS
    @abstractmethod
    def calcular_costo_produccion(self):
        """
        Método abstracto para calcular costo de producción específico.
        Obliga implementación en subclases. (Abstracción, Polimorfismo)
        """
        pass

    @abstractmethod
    def calcular_precio_venta(self):
        """
        Método abstracto para calcular precio de venta específico.
        (Abstracción, Polimorfismo)
        """
        pass

    # Método común para todas las hijas
    def precio_venta_generico(self, margen_extra=0.0):
        """
        Método concreto que usa métodos abstractos para precio genérico.
        Demuestra Template Method pattern. (Abstracción)
        """
        costo = self.calcular_costo_produccion()
        margen = self.__calcular_margen_ganancia() + margen_extra
        return costo * (1 + margen)

    def info_basica(self):
        """
        Devuelve información básica del producto para reportes.
        """
        return f"{self.__codigo} - {self.__nombre} | Stock: {self.__stock}"


class Palomitas(ProductoConfiteria):
    """
    Palomitas de maíz en diferentes tamaños con mantequilla y sal.
    Hereda de ProductoConfiteria (Herencia).
    """
    def __init__(self, codigo, nombre, precio_base, stock, ingredientes, tamaño, mantequilla, sal):
        super().__init__(codigo, nombre, precio_base, stock, ingredientes)
        self.tamaño = tamaño
        self.mantequilla = mantequilla
        self.sal = sal

    def calcular_costo_produccion(self):
        """
        Costo basado en suma de ingredientes.
        Implementación polimórfica simple. (Polimorfismo)
        """
        return sum(self._ingredientes.values())

    def calcular_precio_venta(self):
        """
        Precio con margen extra por tamaño (S:10%, M:20%, L:30%).
        """
        margen_extra = {'S':0.10, 'M':0.20, 'L':0.30}[self.tamaño]
        return round(self.precio_venta_generico(margen_extra), 2)


class Bebida(ProductoConfiteria):
    """
    Bebidas en diferentes tamaños, marcas y tipos (gaseosas con recargo).
    Hereda de ProductoConfiteria (Herencia).
    """
    def __init__(self, codigo, nombre, precio_base, stock, ingredientes, tamaño, marca, es_gaseosa, incluye_hielo):
        super().__init__(codigo, nombre, precio_base, stock, ingredientes)
        self.tamaño = tamaño
        self.marca = marca
        self.es_gaseosa = es_gaseosa
        self.incluye_hielo = incluye_hielo

    def calcular_costo_produccion(self):
        """
        Costo base + 5% extra si es gaseosa.
        """
        base = sum(self._ingredientes.values())
        if self.es_gaseosa:
            base *= 1.05
        return base

    def calcular_precio_venta(self):
        """
        Precio con margen extra fijo del 25%.
        """
        return round(self.precio_venta_generico(0.25), 2)


class Dulce(ProductoConfiteria):
    """
    Dulces nacionales e importados con diferente peso y tipo.
    Hereda de ProductoConfiteria (Herencia).
    """
    def __init__(self, codigo, nombre, precio_base, stock, ingredientes, tipo, peso_gramos, importado):
        super().__init__(codigo, nombre, precio_base, stock, ingredientes)
        self.tipo = tipo
        self.peso_gramos = peso_gramos
        self.importado = importado

    def calcular_costo_produccion(self):
        """
        Costo base + 15% si es importado.
        """
        base = sum(self._ingredientes.values())
        if self.importado:
            base *= 1.15
        return base

    def calcular_precio_venta(self):
        """
        Margen extra: 30% importados, 20% nacionales.
        """
        margen_extra = 0.30 if self.importado else 0.20
        return round(self.precio_venta_generico(margen_extra), 2)


class Combo(ProductoConfiteria):
    """
    Combos promocionales con múltiples productos y descuento.
    Hereda de ProductoConfiteria (Herencia).
    """
    def __init__(self, codigo, nombre, precio_base, stock, ingredientes, productos_incluidos, descuento_combo, popular):
        super().__init__(codigo, nombre, precio_base, stock, ingredientes)
        self.productos_incluidos = productos_incluidos
        self.descuento_combo = descuento_combo
        self.popular = popular

    def calcular_costo_produccion(self):
        """
        Suma costos de productos incluidos + ingredientes del combo.
        """
        costo_total = sum(p.calcular_costo_produccion() for p in self.productos_incluidos)
        costo_total += sum(self._ingredientes.values())
        return costo_total

    def calcular_precio_venta(self):
        """
        Precio de productos con descuento combo + 10% si es popular.
        """
        precio_sin_descuento = sum(p.calcular_precio_venta() for p in self.productos_incluidos)
        precio = precio_sin_descuento * (1 - self.descuento_combo)
        if self.popular:
            precio *= 1.10
        return round(precio, 2)

