from src.models.funciones import FuncionEstreno, PeliculaClasica, Documental, EventoEspecial
from src.models.salas import Sala2D, Sala3D, SalaIMAX, SalaVIP
from src.models.entradas import EntradaGeneral, EntradaInfantil, EntradaEstudiante, ComboPromo
from src.models.confiteria import Palomitas, Bebida, Dulce, Combo

class SistemaCine:
    def __init__(self):
        self.salas = self._crear_salas()
        self.cartelera = self._crear_cartelera()
        self.menu_confiteria = self._crear_menu_confiteria()
        self.entradas_vendidas = []
        self.ingresos_taquilla = 0
        self.ingresos_confiteria = 0


    def _crear_salas(self):
        return [
            Sala2D(1, 100),
            Sala2D(2, 100),
            Sala2D(3, 64),
            Sala2D(4, 64),
            Sala2D(5, 81),
            Sala2D(6, 81),
            Sala2D(7, 36),
            Sala2D(8, 36),
        ]

    def _crear_cartelera(self):
        return [
            FuncionEstreno("A01", "Avengers", 140, "18:00", 1, 69, "Español", "4K"),
            FuncionEstreno("A02", "Dune 2", 155, "20:00", 1, 69, "Ingles", "3D"),
            PeliculaClasica("B01", "El padrino", 175, "16:00", 2, 1972, True, 6),
            PeliculaClasica("B02", "Casablanca", 102, "14:00", 2, 1942, False, 4),
            Documental("C01", "Planeta Tierra", 90, "10:00", 3, "Naturaleza", False, True),
            Documental("C02", "Cosmos", 95, "12:00", 3, "Espacio", True, True),
            EventoEspecial("D01", "Concierto", 110, "22:00", 4, "Musica", False, 20),
            EventoEspecial("D02", "Premios", 130, "19:00", 4, "Cine", True, 20),
        ]

    def _crear_menu_confiteria(self):
        pal1 = Palomitas("P01", "Palomitas S", 8000, 20, {"maiz": 1500, "aceite": 500}, "S", True, True)
        pal2 = Palomitas("P02", "Palomitas M", 10000, 20, {"maiz": 2000, "aceite": 800}, "M", True, True)
        pal3 = Palomitas("P03", "Palomitas L", 12000, 20, {"maiz": 2500, "aceite": 1000}, "L", True, True)

        beb1 = Bebida("B01", "Gaseosa 500ml", 6000, 30, {"liquido": 1200}, "M", "Coca-Cola", True, True)
        beb2 = Bebida("B02", "Agua 600ml", 4000, 30, {"liquido": 800}, "M", "Brisa", False, False)

        dul1 = Dulce("D01", "Chocolate Jet", 3000, 50, {"cacao": 700}, "barra", 30, False)
        dul2 = Dulce("D02", "Chocolate Nordico", 8000, 10, {"cacao": 1500}, "barra", 50, True)

        combo1 = Combo("C01", "Combo Palomitas + Gaseosa", 15000, 10, {}, [pal2, beb1], 0.15, True)

        return [pal1, pal2, pal3, beb1, beb2, dul1, dul2, combo1]

# ----------------- Negocio ---------------------------
    def listar_cartelera(self):
        return self.cartelera

    def listar_menu_confiteria(self):
        return self.menu_confiteria

    def reservar_asientos(self, numero_sala, fila, columna):
        sala = next((s for s in self.salas if s._Sala_numero_sala == numero_sala), None)
        if not sala:
            return False, "Sala no encontrada"
        ok = sala.reservar_asiento(fila, columna)
        return ok, "Reserva realizada" if ok else "No se pudo reservar"

    def vender_entrada_general(self, funcion, asiento, dia_semana, hora_int):
        entrada = EntradaGeneral(
            numero_entrada=len(self.entradas_vendidas) + 1,
            funcion=funcion,
            asiento=asiento,
            precio_base=100,
            dia_semana=dia_semana,
            horario_funcion=hora_int,
        )
        if not entrada.validar_requisitos():
            return False, "Entrada no valida"
        self.entradas_vendidas.append(entrada)
        self.ingresos_taquilla += entrada.calcular_precio_final()
        return True, entrada

    def vender_producto_confiteria(self, codigo, cantidad):
        prod = next((p for p in self.menu_confiteria if p.codigo == codigo), None)
        if not prod:
            return False, "Producto no encontrado"
        if not prod.descontar_stock(cantidad):
            return False, "No se pudo descontar stock"
        self.ingresos_confiteria += prod.calcular_precio_venta() * cantidad
        return True, prod

    def obtener_reporte_ingresos(self):
        return {
            "taquilla": self.ingresos_taquilla,
            "confiteria": self.ingresos_confiteria,
            "total": self.ingresos_taquilla + self.ingresos_confiteria,
        }
