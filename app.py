
from Ablack import ClienteBlack
from Ecompra_dolar import Dolar
from Fretiro_efectivo import Efectivo
from Gtarjeta_credito import TarjetaCredito
from Htran_enviada import Enviado
from obj_cuenta import *
from lecturaJSON import *
from Dchequera import *

pepe=[]

for d in diccionario_transacciones_black:

    p= ClienteBlack(nombre_cliente_black,apellido_cliente_black,numero_cliente,dni_cliente_black,d['estado'])

    cheque= Cheques(d['cupoDiarioRestante'],d['monto'],d['saldoEnCuenta'],d['totalTarjetasDeCreditoActualmente'],d['totalChequerasActualmente'],d['tipo'],p.puede_crear_chequera()) 
    dolar= Dolar(d['cupoDiarioRestante'],d['monto'],d['saldoEnCuenta'],d['totalTarjetasDeCreditoActualmente'],d['totalChequerasActualmente'],d['tipo'],p.puede_comprar_dolar()) 
    efectivo= Efectivo(d['cupoDiarioRestante'],d['monto'],d['saldoEnCuenta'],d['totalTarjetasDeCreditoActualmente'],d['totalChequerasActualmente'],d['tipo'],p.puede_comprar_dolar())
    tarCredito= TarjetaCredito(d['cupoDiarioRestante'],d['monto'],d['saldoEnCuenta'],d['totalTarjetasDeCreditoActualmente'],d['totalChequerasActualmente'],d['tipo'],p.puede_crear_tarjeta_credito())
    enviado= Enviado(d['cupoDiarioRestante'],d['monto'],d['saldoEnCuenta'],d['totalTarjetasDeCreditoActualmente'],d['totalChequerasActualmente'],d['tipo'],True)
    pepe.append(cheque.razonCheque())
    pepe.append(dolar.razonDolar())
    pepe.append(efectivo.razonRetiro())
    pepe.append(tarCredito.razonCredito())
    pepe.append(enviado.razonEnviado())
    #print(cheque.razonCheque())
    #print(dolar.razonDolar())
    #print(efectivo.razonRetiro())
    #print(tarCredito.razonCredito())
    #print(enviado.razonEnviado())
print(pepe)


  
   
   
  
    