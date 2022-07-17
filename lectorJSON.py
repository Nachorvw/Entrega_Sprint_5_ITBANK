import json
class Cliente_Classic:
    def __init__(self, numero, nombre, apellido, dni, tipo, direccion, transacciones):
        self.numero = numero
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.tipo = tipo
        self.direccion_calle = direccion['calle']
        self.direccion_numero = direccion['numero']
        self.direccion_ciudad = direccion['ciudad']
        self.direccion_provincia = direccion['provincia']
        self.direccion_pais = direccion['pais']
        self.transacciones_estado = transacciones['estado']
        self.transacciones_tipo = transacciones['tipo']
        self.transacciones_cuentaNumero = transacciones['cuentaNumero']
        self.transacciones_cupoDiarioRestante = transacciones['cupoDiarioRestante']
        self.transacciones_cantidadExtraccionesHechas = transacciones['cantidadExtraccionesHecha']
        self.transacciones_monto = transacciones['monto']
        self.transacciones_fecha = transacciones['fecha']
        self.transacciones_numero = transacciones['numero']
        self.transacciones_saldoEnCuenta = transacciones['saldoEnCuenta']
        self.transacciones_totalTarjetasDeCreditoActualmente = transacciones['totalTarjetasDeCreditoActualmente']
        self.transacciones_totalChequerasActualmente = transacciones['totalChequerasActualmente']
    @classmethod
    def from_json(cls, json_string):
        json_dict = json.loads(json_string)
        return cls(**json_dict)

    def __repr__(self):
        return f'<user { self.nombre }>'

users_list = []
with open('eventos_classic.json', 'r') as json_file:
    user_data = json.loads(json_file.read())
for u in user_data:
    users_list.append(Cliente_Classic(**u))

print(users_list)