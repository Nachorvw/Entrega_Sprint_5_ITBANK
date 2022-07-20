class Cliente (object):

    def __init__(self,nombre,apellido,numero,dni,cliente):
        self.nombre=nombre
        self.apellido=apellido
        self.numero=numero
        self.dni=dni
        self.cliente=cliente

    def caja_de_ahorro_pesos(self)->bool: 
        return True
          
    def caja_de_ahorro_dolares(self)->bool:
        return True

    def cuenta_corriente(self)->bool:
        return True


