from Tipos_clientes.classic import ClienteClassic
from Tipos_clientes.black import ClienteBlack
from Tipos_clientes.gold import ClienteGold

p=ClienteBlack("german","himmel",1545784515,413967485,"BLACK")
print(p.caja_de_ahorro_pesos())
print(p.caja_de_ahorro_dolares())
print(p.cuenta_corriente())
