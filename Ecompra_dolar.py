from Ablack import *
from obj_cuenta import *

class Dolar (object):
    def __init__(self,limite,monto,saldo,totalTarjetasDeCredito,totalChequeras,tipo,dolar):
        self.limite=limite
        self.monto=monto
        self.saldo=saldo
        self.totalTarjetas=totalTarjetasDeCredito
        self.totalChequeras=totalChequeras
        self.tipo=tipo
        self.dolar=dolar
        
    def razonDolar (self):
        if self.tipo=="COMPRA_DOLAR":
            if self.dolar :
                if self.limite <= self.monto:
                    return "Superaste el limite"