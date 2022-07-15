from Tipos_clientes.cliente import Cliente

class ClienteClassic (Cliente):
    def puede_crear_chequera(self)->bool: 
        return False
    def puede_crear_tarjeta_credito(self)->bool:
        return False
    def puede_comprar_dolar(self)->bool:
        return False

