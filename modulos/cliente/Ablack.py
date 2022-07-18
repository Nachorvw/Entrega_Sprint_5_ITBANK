from modulos.cliente.obj_cliente import Cliente
from modulos.lecturaJSON import *

class ClienteBlack (Cliente):
    def puede_crear_chequera(self)->bool: 
        return True
    def puede_crear_tarjeta_credito(self)->bool:
        return True
    def puede_comprar_dolar(self)->bool:
        return True
    def caja_de_ahorro_pesos(self)->bool: 
        return True     
    def caja_de_ahorro_dolares(self)->bool:
        return True
    def cuenta_corriente(self)->bool:
        return True

