from modulos.cliente.Ablack import *
from modulos.obj_cuenta import *

class Enviado (object):
    def __init__(self,limite,monto,saldo,totalTarjetasDeCredito,totalChequeras,tipo,envio):
        self.limite=limite
        self.monto=monto
        self.saldo=saldo
        self.totalTarjetas=totalTarjetasDeCredito
        self.totalChequeras=totalChequeras
        self.tipo=tipo
        self.envio=envio
        
    def razonEnviado(self):
        if self.tipo=="TRANSFERENCIA_ENVIADA":
            if self.envio:
                if self.monto>=self.limite:
                    return "Superas el limite, maximo por dia"
            