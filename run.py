from archivos_para_html.pagina import creaHTML, tablaHTML
from modulos.lecturaJSON import diccionario_transacciones_black
from app import listaRazones
#Carga los datos al archivo html 
prueba=creaHTML()
for d in diccionario_transacciones_black:
    pepe=tablaHTML(d["fecha"],d["tipo"],d["estado"],d["monto"],listaRazones[d["numero"]-1])
  

