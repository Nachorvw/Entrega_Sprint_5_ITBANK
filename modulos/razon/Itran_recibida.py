
from modulos.cliente.Ablack import *
from modulos.obj_cuenta import *

class Recibida (object):
    def __init__(self,limite,monto,saldo,totalTarjetasDeCredito,totalChequeras,tipo,recivida):
        self.limite=limite
        self.monto=monto
        self.saldo=saldo
        self.totalTarjetas=totalTarjetasDeCredito
        self.totalChequeras=totalChequeras
        self.tipo=tipo
        self.recivida=recivida
        
    def razonRecibida(self):
        if self.tipo=="TRANSFERENCIA_RECIBIDA":
            if self.recivida:
                if self.monto>=600000:
                    return "Superate el monto maximo"
            