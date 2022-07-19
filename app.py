
from modulos.cliente.Ablack import ClienteBlack
from modulos.razon.Ecompra_dolar import Dolar
from modulos.razon.Fretiro_efectivo import Efectivo
from modulos.razon.Gtarjeta_credito import TarjetaCredito
from modulos.razon.Htran_enviada import Enviado
from modulos.obj_cuenta import *
from modulos.lecturaJSON import *
from modulos.razon.Dchequera import *

listaRazones=[]

for d in diccionario_transacciones_black:

    p= ClienteBlack(nombre_cliente_black,apellido_cliente_black,numero_cliente,dni_cliente_black,d['estado'])

    cheque= Cheques(d['cupoDiarioRestante'],d['monto'],d['saldoEnCuenta'],d['totalTarjetasDeCreditoActualmente'],d['totalChequerasActualmente'],d['tipo'],p.puede_crear_chequera()) 
    dolar= Dolar(d['cupoDiarioRestante'],d['monto'],d['saldoEnCuenta'],d['totalTarjetasDeCreditoActualmente'],d['totalChequerasActualmente'],d['tipo'],p.puede_comprar_dolar()) 
    efectivo= Efectivo(d['cupoDiarioRestante'],d['monto'],d['saldoEnCuenta'],d['totalTarjetasDeCreditoActualmente'],d['totalChequerasActualmente'],d['tipo'],p.puede_comprar_dolar())
    tarCredito= TarjetaCredito(d['cupoDiarioRestante'],d['monto'],d['saldoEnCuenta'],d['totalTarjetasDeCreditoActualmente'],d['totalChequerasActualmente'],d['tipo'],p.puede_crear_tarjeta_credito())
    enviado= Enviado(d['cupoDiarioRestante'],d['monto'],d['saldoEnCuenta'],d['totalTarjetasDeCreditoActualmente'],d['totalChequerasActualmente'],d['tipo'],True)
    if cheque.razonCheque():
        listaRazones.append(cheque.razonCheque())
    elif dolar.razonDolar():
        listaRazones.append(dolar.razonDolar())
    elif efectivo.razonRetiro():
        listaRazones.append(efectivo.razonRetiro())
    elif tarCredito.razonCredito():
        listaRazones.append(tarCredito.razonCredito())
    elif enviado.razonEnviado():
        listaRazones.append(enviado.razonEnviado())
    else: listaRazones.append("ACEPTADA")

print(listaRazones)


  
   
   
  
    