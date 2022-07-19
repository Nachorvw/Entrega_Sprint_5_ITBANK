import webbrowser
from app import p
from modulos import lecturaJSON


#Recorro la informacion del cliente para obtener su direccion
direct=lecturaJSON.data_black['direccion']
direcciones= f"{direct['calle']} {direct['numero']}, {direct['ciudad']}, {direct['provincia']}, {direct['pais']} "


def creaHTML():
    
    nombre=f"{p.nombre}, {p.apellido}"
    numeroCliente=lecturaJSON.numero_cliente
    DNI=p.dni
    direccion=direcciones
    #Abro el archivo HTML
    fun = open('index.html', 'w')
    #Le doy la forma al archivo html
    html_template = f"""
    <html>
        <head>
            <title>Historial de Transacciones</title>
            <link rel="stylesheet" href="archivos_para_html/estilos.css">
        </head>
        <body>
            <h1>{nombre}</h1>
            <div>Numero de Cliente: {numeroCliente}</div>
            <div>Dni: {DNI}</div>
            <div>Direccion: {direccion}</div>
        </body>
    </html>
    <table>
            <tr><td>Fecha</td><td>Tipo</td><td>Estado</td><td>Monto</td><td>Razon</td></tr>
    """
    #Sobre escribo el archivo html con el diseño anterior
    fun.write(html_template)
    if __name__ == '__main__':
        creaHTML()

def tablaHTML (fecha,tipo,estado,monto,razon):
    car = open('index.html', 'a')
    html_tabla=f"""
            <tr><td>{fecha}</td><td>{tipo}</td><td>{estado}</td><td>{monto}</td><td>{razon}</td></tr>
            """

    car.write(html_tabla)
    if __name__ == '__main__':
        tablaHTML()