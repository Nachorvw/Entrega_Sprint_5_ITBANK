import json
from modulos.obj_cuenta import *

#------------------------------
diccionario_transacciones_black = []
transacciones_estado_black = dict()
nombre_cliente_black = ""
apellido_cliente_black = ""
dni_cliente_black = ""
tipo_cliente_black = ""
numero_cliente=""
direccion_cliente_black = []

#------------------------------------------
#usuarios BLACK
with open("eventos_classic.json") as black:
    data_json_black = black.read()
    data_black = json.loads(data_json_black)
# print(data_black)
for transaccion in data_black["transacciones"]:
     diccionario_transacciones_black.append(transaccion)
    
for datos in data_black:
    nombre_cliente_black = data_black['nombre']
    apellido_cliente_black = data_black['apellido']
    dni_cliente_black = data_black['dni']
    tipo_cliente_black = data_black['tipo']
    numero_cliente=data_black['numero']

#--------------------------------------------

# print(json.dumps(data_classic, indent=2))
""" print(nombre_cliente_black)
print(apellido_cliente_black)
print(dni_cliente_black)
print(tipo_cliente_black)
print(data_black['direccion']['calle'])
print(data_black['direccion']['numero'])
print(data_black['direccion']['ciudad'])
print(data_black['direccion']['pais'])
print(data_black['direccion']['provincia'])
print(diccionario_transacciones_black[0]['estado'])
print(diccionario_transacciones_black) 
 """



