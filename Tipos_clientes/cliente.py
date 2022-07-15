""" def validacion(valor):
    return isinstance(valor,(int,float,complex))



class Punto (object):
    def __init__(self,x=0,y=0):
        if validacion(x) and validacion(y):
            self.x=x
            self.y=y
        else :
            return TypeError ("x e y tienen que ser valores numericos")
    def distncia(self, otro):
        r = self.restar(otro)
        return r.norma()

    def restar (self,otro):

        return (self.x-otro.x, self.y-otro.y)

    def norma(self):

        return (self.x*self.x+self.y*self.y)
    
    def __str__(self):

        return "("+str(self.x)+","+str(self.y)+")"
        

p = Punto(5,7)
q=Punto(2,3)
print(p.x)
print(p.y)
print(p) """

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
        if (self.cliente == ("CLASSIC")):
            return False

        elif (self.cliente == ("BLACK")):
            return True

        else: return True
