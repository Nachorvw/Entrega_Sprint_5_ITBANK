from Tipos_clientes.cliente import Cliente

class ClienteBlack (Cliente):
    def puede_crear_chequera(self)->bool: 
        return True
    def puede_crear_tarjeta_credito(self)->bool:
        return True
    def puede_comprar_dolar(self)->bool:
        return True