
from Ablack import *
from obj_cuenta import *

""" class Cheques (ClienteBlack):
    def resol (p):
        if not p.puede_crear_chequera():
            return "No puede crear Cheque"
        
        else:
            return p.apellido """


""" class Cheques (object):
    def __init__(self,limite,monto,saldo,totalTarjetasDeCredito,totalChequeras):
        self.limite=limite
        self.monto=monto
        self.saldo=saldo
        self.totalTarjetas=totalTarjetasDeCredito
        self.totalChequeras=totalChequeras

    def resol (self,p:ClienteBlack):
        if not p.puede_crear_chequera():
            return "No puede crear Cheque"
        
        else:
            return p.apellido
         """
        
class Cheques (object):
    def __init__(self,limite,monto,saldo,totalTarjetasDeCredito,totalChequeras,tipo,cheque):
        self.limite=limite
        self.monto=monto
        self.saldo=saldo
        self.totalTarjetas=totalTarjetasDeCredito
        self.totalChequeras=totalChequeras
        self.tipo=tipo
        self.cheque=cheque
        
    def razonCheque (self):
        if self.tipo=="ALTA_CHEQUERA":
            if self.cheque :
                if self.totalChequeras >= 2:
                    return "tiene muchas chequetas, No puedes crear una mas"

