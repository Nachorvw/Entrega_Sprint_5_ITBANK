
class Cuenta (object):
    def __init__(self,limite,monto,saldo,totalTarjetasDeCredito,totalChequeras):
        self.limite=limite
        self.tran_recibida=totalChequeras
        self.monto=monto
        self.totalTarjetasDeCredito=totalTarjetasDeCredito
        self.saldo=saldo
        
