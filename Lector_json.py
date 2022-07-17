import json
from subprocess import call


diccionario_transacciones = []
nombre_cliente = ""
apellido_cliente = ""
dni_cliente = ""
tipo_cliente = ""
direccion_cliente = []

with open("eventos_classic.json") as classic:
    data = json.load(classic)
# print(data)
for transaccion in data["transacciones"]:
     diccionario_transacciones.append(transaccion)

for direccion in data['direccion']:
    direccion_cliente.append(direccion['calle'])
    direccion_cliente.append(direccion['numero'])
    direccion_cliente.append(direccion['ciudad'])
    direccion_cliente.append(direccion['provincia'])
    direccion_cliente.append(direccion['pais'])



for datos in data:
    nombre_cliente = data['nombre']
    apellido_cliente = data['apellido']
    dni_cliente = data['dni']
    tipo_cliente = data['tipo']
    
    

print(nombre_cliente)
print(apellido_cliente)
print(dni_cliente)
print(tipo_cliente)
print(direccion['calle'])
print(direccion['numero'])
print(direccion['ciudad'])
print(direccion['provincia'])
print(direccion['pais'])
print(diccionario_transacciones[0])