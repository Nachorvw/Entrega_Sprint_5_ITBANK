import webbrowser
from app import p

def creaHTML():
    
    
    nombre=p.nombre 
    numeroCliente=p.cliente
    DNI=p.dni
    direccion=p.nombre
    #Abro el archivo HTML
    fun = open('index.html', 'w')
    #Le doy la forma al archivo html
    html_template = f"""
    <html>
        <head>
            <title>Title</title>
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