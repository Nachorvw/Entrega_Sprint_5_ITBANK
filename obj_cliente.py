class Cliente (object):

    def __init__(self,nombre,apellido,numero,dni,cliente):
        self.nombre=nombre
        self.apellido=apellido
        self.numero=numero
        self.dni=dni
        self.cliente=cliente

    def caja_de_ahorro_pesos(self)->bool: 
        if (self.cliente == ("CLASSIC")):
            return True
            
        elif (self.cliente == ("BLACK")):
            return True

        else: return True
          
    def caja_de_ahorro_dolares(self)->bool:
        if (self.cliente == ("CLASSIC")):
            return False
            
        elif (self.cliente == ("BLACK")):
            return True

        else: return True


    def cuenta_corriente(self)->bool:
        if (self.cliente == ("RECHAZADA")):
            return False

        elif (self.cliente == ("ACEPTADA")):
            return True

        else: return True


