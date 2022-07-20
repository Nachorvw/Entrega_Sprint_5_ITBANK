from modulos.cliente.Ablack import *
from modulos.obj_cuenta import *

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
                if self.totalTarjetas>=5:
                    return "Superaste el limite, de tarjetas de credito"
                elif self.monto>self.limite:
                    return "Superaste el limite, de cupo diario" 
            
                return "no esta habilitado para dar de alta una tarjeta de credito"
            

