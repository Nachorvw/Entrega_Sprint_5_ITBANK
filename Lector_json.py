import json
from subprocess import call
from urllib import response


diccionario_transacciones = []
transacciones_estado = dict()
nombre_cliente = ""
apellido_cliente = ""
dni_cliente = ""
tipo_cliente = ""
direccion_cliente = []

with open("eventos_classic.json") as classic:
    data_json_classic = classic.read()
    data_classic = json.loads(data_json_classic)
# print(data_classic)
for transaccion in data_classic["transacciones"]:
     diccionario_transacciones.append(transaccion)
     
     
     
for datos in data_classic:
    nombre_cliente = data_classic['nombre']
    apellido_cliente = data_classic['apellido']
    dni_cliente = data_classic['dni']
    tipo_cliente = data_classic['tipo']
    
    
# print(json.dumps(data_classic, indent=2))
print(nombre_cliente)
print(apellido_cliente)
print(dni_cliente)
print(tipo_cliente)
print(data_classic['direccion']['calle'])
print(data_classic['direccion']['numero'])
print(data_classic['direccion']['ciudad'])
print(data_classic['direccion']['pais'])
print(data_classic['direccion']['provincia'])
print(diccionario_transacciones[0]['estado'])