import json
from subprocess import call
from urllib import response


diccionario_transacciones_classic = []
transacciones_estado_classic = dict()
nombre_cliente_classic = ""
apellido_cliente_classic = ""
dni_cliente_classic = ""
tipo_cliente_classic = ""
direccion_cliente_classic = []
#----------------------------
diccionario_transacciones_gold = []
transacciones_estado_gold = dict()
nombre_cliente_gold = ""
apellido_cliente_gold = ""
dni_cliente_gold = ""
tipo_cliente_gold = ""
direccion_cliente_gold = []
#------------------------------
diccionario_transacciones_black = []
transacciones_estado_black = dict()
nombre_cliente_black = ""
apellido_cliente_black = ""
dni_cliente_black = ""
tipo_cliente_black = ""
direccion_cliente_black = []
#------------------------------
#usuarios CLASSIC
with open("eventos_classic.json") as classic:
    data_json_classic = classic.read()
    data_classic = json.loads(data_json_classic)
# print(data_classic)
for transaccion in data_classic["transacciones"]:
     diccionario_transacciones_classic.append(transaccion)
    
for datos in data_classic:
    nombre_cliente = data_classic['nombre']
    apellido_cliente = data_classic['apellido']
    dni_cliente = data_classic['dni']
    tipo_cliente = data_classic['tipo']
#----------------------------------------
#usuarios GOLD   
with open("eventos_gold.json") as gold:
    data_json_gold = gold.read()
    data_gold = json.loads(data_json_gold)

for transaccion in data_gold["transacciones"]:
     diccionario_transacciones_gold.append(transaccion)

for datos in data_gold:
    nombre_cliente_gold = data_gold['nombre']
    apellido_cliente_gold = data_gold['apellido']
    dni_cliente_gold = data_gold['dni']
    tipo_cliente_gold= data_gold['tipo']
#------------------------------------------
#usuarios BLACK
with open("eventos_black.json") as black:
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
#--------------------------------------------

# print(json.dumps(data_classic, indent=2))
print(nombre_cliente_black)
print(apellido_cliente_black)
print(dni_cliente_black)
print(tipo_cliente_black)
print(data_black['direccion']['calle'])
print(data_black['direccion']['numero'])
print(data_black['direccion']['ciudad'])
print(data_black['direccion']['pais'])
print(data_black['direccion']['provincia'])
print(diccionario_transacciones_black[0]['estado'])