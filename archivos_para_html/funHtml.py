import webbrowser

def creaHTML():
    
    
    nombre="Gabriel, Moreno"
    numeroCliente="450066"
    DNI="2947744"
    direccion="tu casita 12345"
    #Abro el archivo HTML
    fun = open('index.html', 'w')
    #Le doy la forma al archivo html
    html_template = f"""
    <html>
        <head>
            <title>Title</title>
            <link rel="stylesheet" href="/html/style.css">
        </head>
        <body>
            <h1>{nombre}</h1>
            <div>Numero de Cliente: {numeroCliente}</div>
            <div>Dni: {DNI}</div>
            <div>Direccion: {direccion}</div>
            <table>
            <tr><td>Fecha</td><td>Tipo</td><td>Estado</td><td>Monto</td><td>Razon</td></tr>
            <tr><td>a</td><td>aaaaaaaaaaaaaaaaaaaa</td><td>aaaaaaaaaaa</td><td>aaaaaaaaaaa</td><td>aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa</td></tr>
            <tr><td>b</td><td></td><td></td><td></td><td>b</td></tr>
            <tr><td>c</td><td></td><td></td><td></td><td>c</td></tr>
            123
            </table>
        </body>
    </html>
    """
    #Sobre escribo el archivo html con el diseño anterior
    fun.write(html_template)
    if __name__ == '__main__':
        creaHTML()