from Ablack import *
from obj_cuenta import *

class TarjetaCredito (object):
    def __init__(self,limite,monto,saldo,totalTarjetasDeCredito,totalChequeras,tipo,credito):
        self.limite=limite
        self.monto=monto
        self.saldo=saldo
        self.totalTarjetas=totalTarjetasDeCredito
        self.totalChequeras=totalChequeras
        self.tipo=tipo
        self.credito=credito
        
    def razonCredito(self):
        if self.tipo=="ALTA_TARJETA_CREDITO":
            if self.credito:
                if self.totalTarjetas>5:
                    return "Superaste el limite, de tarjetas de credito"
            

