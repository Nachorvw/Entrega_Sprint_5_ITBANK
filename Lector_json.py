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
    data_json = classic.read()
    data = json.loads(data_json)
# print(data)
for transaccion in data["transacciones"]:
     diccionario_transacciones.append(transaccion)
     
     
     
for datos in data:
    nombre_cliente = data['nombre']
    apellido_cliente = data['apellido']
    dni_cliente = data['dni']
    tipo_cliente = data['tipo']
    
    
# print(json.dumps(data, indent=2))
print(nombre_cliente)
print(apellido_cliente)
print(dni_cliente)
print(tipo_cliente)
print(data['direccion']['calle'])
print(data['direccion']['numero'])
print(data['direccion']['ciudad'])
print(data['direccion']['pais'])
print(data['direccion']['provincia'])
print(diccionario_transacciones[0]['estado'])