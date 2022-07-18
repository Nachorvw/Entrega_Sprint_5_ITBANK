from modulos.cliente.Ablack import *
from modulos.obj_cuenta import *

class Efectivo (object):
    def __init__(self,limite,monto,saldo,totalTarjetasDeCredito,totalChequeras,tipo,efectivo):
        self.limite=limite
        self.monto=monto
        self.saldo=saldo
        self.totalTarjetas=totalTarjetasDeCredito
        self.totalChequeras=totalChequeras
        self.tipo=tipo
        self.efectivo=efectivo
        
    def razonRetiro(self):
        if self.tipo=="RETIRO_EFECTIVO_CAJERO_AUTOMATICO":
                if self.monto>self.limite:
                    return "Superaste el limite"
            

