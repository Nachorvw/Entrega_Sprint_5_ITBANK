from modulos.cliente.obj_cliente import Cliente
from modulos.lecturaJSON import *

class ClienteClassic (Cliente):
    def puede_crear_chequera(self)->bool: 
        return False
    def puede_crear_tarjeta_credito(self)->bool:
        return False
    def puede_comprar_dolar(self)->bool:
        return False
    def caja_de_ahorro_pesos(self)->bool: 
        return True     
    def caja_de_ahorro_dolares(self)->bool:
        return False
    def cuenta_corriente(self)->bool:
        return False


