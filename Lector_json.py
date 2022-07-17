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
    
    
# print(json.dumps(data_classic, indent=2))
# print(nombre_cliente_classic)
# print(apellido_cliente_classic)
# print(dni_cliente_classic)
# print(tipo_cliente_classic)
# print(data_classic['direccion']['calle'])
# print(data_classic['direccion']['numero'])
# print(data_classic['direccion']['ciudad'])
# print(data_classic['direccion']['pais'])
# print(data_classic['direccion']['provincia'])
# print(diccionario_transacciones_classic[0]['estado'])